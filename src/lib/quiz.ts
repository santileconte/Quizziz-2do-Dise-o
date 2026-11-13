import { grade, normalize } from './match'

export type UnitKey = 'b1' | 'b2' | 'b3' | 'b4' | 'b5' | 'b6' | 'b7'

/**
 * De dónde sale la pregunta. Las tres primeras son de la cátedra y se conservan literales;
 * las otras son práctica y nunca cuentan como evidencia de lo que se toma.
 */
export type Modalidad = 'parcial' | 'simulacro' | 'cuestionario' | 'practica' | 'quizziz' | 'ia' | 'propia'

export const modalidades: { key: Modalidad; label: string; tag: string; hint: string; original: boolean }[] = [
  {
    key: 'parcial',
    label: 'Parcial y recuperatorio 2024',
    tag: 'Parcial real',
    hint: 'Las 32 consignas del parcial y del recuperatorio de teoría de 2024, tal como figuran en las capturas.',
    original: true,
  },
  {
    key: 'simulacro',
    label: 'Simulación 2024',
    tag: 'Simulación de la cátedra',
    hint: 'Simulación Parcial 2 del aula virtual (2024): dos intentos con preguntas distintas del mismo banco.',
    original: true,
  },
  {
    key: 'cuestionario',
    label: 'Cuestionarios 2026',
    tag: 'Cuestionario semanal',
    hint: 'Cuestionarios semanales de este año. El texto llega por una transcripción, no por las capturas originales.',
    original: true,
  },
  {
    key: 'practica',
    label: 'Figuras y diagramas de la cátedra',
    tag: 'Práctica de la cátedra',
    hint: 'Figuras de patrones GoF y diagramas de los flujos del PUDS del simulador de la cátedra («Simulacro_DSI_solo_material_base.pdf»).',
    original: true,
  },
  {
    key: 'quizziz',
    label: 'Quizziz',
    tag: 'Quizziz',
    hint: 'Preguntas de cuestionarios que solo aparecen en el Quizziz. Las demás preguntas del Quizziz ya estaban en otros registros y no se repiten.',
    original: true,
  },
  {
    key: 'ia',
    label: 'Generadas con IA (carpeta)',
    tag: 'Generada con IA',
    hint: 'Preguntas que ya venían generadas con IA en dos documentos de la carpeta. No son de la cátedra.',
    original: false,
  },
  {
    key: 'propia',
    label: 'Nuevas de este repaso',
    tag: 'Pregunta nueva',
    hint: 'Escritas para este repaso a partir del apunte y las diapositivas. No son de la cátedra.',
    original: false,
  },
]

export const modalidadDe = (m: Modalidad) => modalidades.find((x) => x.key === m)!
export type Formato = 'mc' | 'multi' | 'vf' | 'rel' | 'fill' | 'tabla' | 'dev'

/** Celda de un cuadro: texto fijo, hueco para escribir (r) o hueco con opciones (r + o). */
export type Celda = string | { r: string; alt?: string[]; o?: string[] }

interface Comun {
  tema: string
  /** Enunciado. */
  q: string
  /** Por qué es así. Se muestra al corregir. */
  e?: string
  /** Clave de un caso de `casos.ts` que se muestra arriba del enunciado. */
  ctx?: string
  /** Archivo y página, imagen o ítem de donde salió. */
  src?: string
  /** Código que acompaña al enunciado. */
  code?: string
  /** Figuras del enunciado: nombres de archivo de `src/cuestionarios/img/`. */
  img?: string[]
  /** Clave sin confirmar: se puede responder y ver la clave propuesta, pero no suma puntaje hasta verificarla. */
  dud?: string
  /** Parte del texto no es el original de la cátedra: qué se reconstruyó. */
  recon?: string
  /** Opciones (índices de `o`) total o parcialmente reconstruidas: se marcan al lado de la opción. */
  oRecon?: number[]
  /** Quién y cómo confirmó una clave que estaba en duda. Lo completa `verificadas.ts`. */
  verif?: string
  /** Dónde repasar el tema: apunte, diapositivas o libro, con página. */
  ref?: string
  /** La clave no viene de la cátedra: la puso quien generó la pregunta. */
  inf?: boolean
  /** Aclaración sobre la clave o la consigna original. */
  nota?: string
}

export type ItemDef = Comun &
  (
    /** `oi`: figura de cada opción (o null), en el mismo orden que `o`. */
    | { t: 'mc'; o: string[]; a: number; oi?: (string | null)[] }
    | { t: 'multi'; o: string[]; a: number[]; oi?: (string | null)[] }
    /** [afirmación, es verdadera, por qué (opcional)] */
    | { t: 'vf'; i: [string, boolean, string?][] }
    /** [elemento, respuesta]; `extra` agrega distractores a las opciones. */
    | { t: 'rel'; i: [string, string][]; extra?: string[] }
    /** [texto con ___ o etiqueta, respuesta, otras respuestas válidas] */
    | { t: 'fill'; i: [string, string, string[]?][] }
    | { t: 'tabla'; c: string[]; f: Celda[][] }
    /** Consigna de desarrollo: respuesta modelo y puntos que tiene que tocar. */
    | { t: 'dev'; m: string; k?: string[] }
  )

export type Question = ItemDef & { id: string; unit: UnitKey; modalidad: Modalidad }

export interface Answer {
  /** mc */
  n?: number | null
  /** multi */
  ns?: number[]
  /** vf */
  bs?: (boolean | null)[]
  /** rel, fill, tabla (un valor por hueco) y dev (texto en la posición 0) */
  ss?: string[]
  /** dev: autocorrección (1, 0.5 o 0) */
  self?: number | null
}

export const formatoLabel: Record<Formato, string> = {
  mc: 'Choice',
  multi: 'Selección múltiple',
  vf: 'Verdadero o falso',
  rel: 'Relacionar',
  fill: 'Completar',
  tabla: 'Completar cuadro',
  dev: 'Desarrollo',
}

export const celdasHueco = (q: Extract<ItemDef, { t: 'tabla' }>) =>
  q.f.flat().filter((c): c is Exclude<Celda, string> => typeof c !== 'string')

/** Respuestas posibles de una consigna de relacionar, sin repetir. */
export const opcionesRel = (q: Extract<ItemDef, { t: 'rel' }>) =>
  [...new Set([...q.i.map(([, r]) => r), ...(q.extra ?? [])])].sort((a, b) => a.localeCompare(b, 'es'))

/** Opciones que dependen de su posición ("a y b son correctas") no se pueden mezclar. */
const fijas = /ningun|todas las|anteriores|\b[a-g] y [a-g]\b/i
export const sePuedeMezclar = (o: string[]) => !o.some((x) => fijas.test(x))

const ok = (input: string | undefined, answer: string, accept?: string[]) =>
  grade(input ?? '', { answer, accept }).grade !== 'bad'

/** La pregunta suma al puntaje y al progreso. Las de clave en duda no, hasta que se verifiquen. */
export const puntua = (q: Question) => !q.dud

/**
 * Partes correctas de la respuesta y nota de 0 a 1.
 * Selección múltiple puntúa como en las revisiones de Moodle de 2024: cada opción correcta suma su parte
 * y cada incorrecta resta lo mismo, sin bajar de cero (una correcta y una incorrecta dieron 0 en el parcial).
 */
export function corregir(q: Question, a: Answer | undefined): { score: number; parts: boolean[] } {
  let parts: boolean[]
  switch (q.t) {
    case 'mc':
      parts = [a?.n === q.a]
      break
    case 'multi': {
      const elegidas = a?.ns ?? []
      const bien = elegidas.filter((i) => q.a.includes(i)).length
      const mal = elegidas.length - bien
      const score = Math.max(0, (bien - mal) / q.a.length)
      return { score, parts: [score === 1] }
    }
    case 'vf':
      parts = q.i.map(([, v], i) => a?.bs?.[i] === v)
      break
    case 'rel':
      parts = q.i.map(([, r], i) => normalize(a?.ss?.[i] ?? '') === normalize(r))
      break
    case 'fill':
      parts = q.i.map(([, r, alt], i) => ok(a?.ss?.[i], r, alt))
      break
    case 'tabla':
      parts = celdasHueco(q).map((c, i) =>
        c.o ? normalize(a?.ss?.[i] ?? '') === normalize(c.r) : ok(a?.ss?.[i], c.r, c.alt),
      )
      break
    case 'dev':
      return { score: a?.self ?? 0, parts: [(a?.self ?? 0) === 1] }
  }
  return { score: parts.filter(Boolean).length / parts.length, parts }
}

/** Respondió algo: para avisar antes de entregar. */
export function respondida(q: Question, a: Answer | undefined) {
  if (!a) return false
  switch (q.t) {
    case 'mc':
      return a.n !== undefined && a.n !== null
    case 'multi':
      return !!a.ns?.length
    case 'vf':
      return q.i.every((_, i) => a.bs?.[i] !== undefined && a.bs?.[i] !== null)
    case 'dev':
      return !!a.ss?.[0]?.trim()
    default:
      return !!a.ss?.some((s) => s?.trim())
  }
}

/** Mezcla estable para que las opciones no cambien de lugar entre renders. */
export function ordenOpciones(id: string, n: number, intento: number) {
  let h = intento + 7
  for (const c of id) h = (h * 31 + c.charCodeAt(0)) >>> 0
  const orden = Array.from({ length: n }, (_, i) => i)
  for (let i = n - 1; i > 0; i--) {
    h = (h * 1103515245 + 12345) >>> 0
    const j = h % (i + 1)
    ;[orden[i], orden[j]] = [orden[j], orden[i]]
  }
  return orden
}

export function mezclar<T>(xs: T[]) {
  const out = [...xs]
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[out[i], out[j]] = [out[j], out[i]]
  }
  return out
}
