import data from '../figuras/figuras.json'
import { figura } from '../cuestionarios'
import { questions } from '../cuestionarios'
import { temario, type Tema, type Prioridad } from '../temario'

/**
 * Figuras originales de los materiales, agrupadas por tema.
 *
 * Se generan con `tools/figuras/` a partir de los PDF de la carpeta: cada figura distinta aparece una sola vez,
 * con todas las páginas en las que está. Las versiones con diferencias relevantes (otra traducción, otra
 * resolución con texto distinto, una versión con casilleros vacíos) son figuras separadas.
 *
 * Orden dentro de cada tema (`rank`):
 *   1 · Parcial real: la figura, o su versión con casilleros vacíos, se tomó en el parcial o el recuperatorio 2024.
 *   2 · Cátedra: aparece en la Simulación 2024, en un cuestionario 2026 o en la práctica de la cátedra.
 *   3 · Clase: está en las diapositivas de clase (PF) o en el Word de la cátedra (WM).
 *   4 · Apunte base: solo en el apunte de Celina.
 *   5 · Complementaria: solo en otros apuntes (Copia, Fidanza).
 * Dentro de cada nivel van primero las que están en más archivos y después por orden de clase.
 */

export interface Ref {
  archivo: string
  corto?: string
  pag?: number
  nota?: string
}

export interface Figura {
  id: string
  tema: string
  orden: number
  rank: 1 | 2 | 3 | 4 | 5
  nivel: string
  title: string | null
  w: number
  h: number
  refs: Ref[]
  /** Archivo de la página que se muestra (cuando la figura está en varias). */
  mostrada?: string
  tipo: string
  nota?: string | null
  legib?: string | null
  /** Figuras que vienen de una pregunta (están en src/cuestionarios/img). */
  qimg?: string
  preguntas?: string[]
}

const full = import.meta.glob('../figuras/img/*.webp', { eager: true, query: '?url', import: 'default' }) as Record<string, string>
const thumbs = import.meta.glob('../figuras/thumb/*.webp', { eager: true, query: '?url', import: 'default' }) as Record<string, string>

export const figuras = (data as { figuras: Figura[] }).figuras
const tambien = (data as { tambien: Record<string, string[]> }).tambien

export const imagenDe = (f: Figura) => (f.qimg ? figura(f.qimg) : full[`../figuras/img/${f.id}.webp`])
export const miniaturaDe = (f: Figura) => thumbs[`../figuras/thumb/${f.id}.webp`] ?? imagenDe(f)

const porId = new Map(figuras.map((f) => [f.id, f]))

/** Figuras propias del tema, ya ordenadas por prioridad. */
export const figurasDe = (n: string) => figuras.filter((f) => f.tema === n).sort((a, b) => a.orden - b.orden)

/** Figuras de otros temas que también sirven para este (por ejemplo, los cinco flujos en el repaso). */
export const relacionadasDe = (n: string) => (tambien[n] ?? []).map((id) => porId.get(id)!).filter(Boolean)

export const niveles: { rank: Figura['rank']; titulo: string; detalle: string }[] = [
  { rank: 1, titulo: 'Tomadas en parciales reales', detalle: 'La figura, o su versión con casilleros vacíos, se tomó en el parcial o en el recuperatorio 2024.' },
  { rank: 2, titulo: 'Usadas por la cátedra', detalle: 'Aparecen en la Simulación 2024, en un cuestionario 2026 o en la práctica de la cátedra.' },
  { rank: 3, titulo: 'Mostradas en clase', detalle: 'Diapositivas de clase (PF) y Word de la cátedra (WM).' },
  { rank: 4, titulo: 'Apunte base', detalle: 'Solo en el apunte de Celina.' },
  { rank: 5, titulo: 'Complementarias', detalle: 'Solo en otros apuntes (Copia, Fidanza). Disponibles para consultar.' },
]

export const archivos: Record<string, string> = {
  PF: 'PF_Powers_de_Clase_364p.pdf',
  WM: 'WM_Microservicios_del_Word.pdf',
  Celina: 'Apunte Segundo Parcial - Celina.pdf',
  Copia: 'Copia de Apunte Diseño.pdf',
  Fidanza: 'ApunteDiseñoSistemasInformación.pdf',
}

const PRIO_ORDEN: Record<Prioridad, number> = { A: 0, B: 1, C: 2, Cond: 3, Pend: 4 }

/** Consignas del parcial y del recuperatorio 2024 de cada tema (no cuenta copias). */
export const consignasReales = (t: Tema) =>
  questions.filter((q) => t.temas.includes(q.tema) && (q.id.startsWith('p24') || q.id.startsWith('r24'))).length

/** Temas con figuras, ordenados por importancia: prioridad, consignas reales, figuras de examen y orden de clase. */
export const temasPorImportancia = (lista: Tema[] = temario) =>
  lista
    .map((t) => ({ t, figs: figurasDe(t.n), rel: relacionadasDe(t.n), reales: consignasReales(t) }))
    .filter((x) => x.figs.length + x.rel.length > 0)
    .sort(
      (a, b) =>
        PRIO_ORDEN[a.t.prio] - PRIO_ORDEN[b.t.prio] ||
        b.reales - a.reales ||
        b.figs.filter((f) => f.rank <= 2).length - a.figs.filter((f) => f.rank <= 2).length ||
        temario.indexOf(a.t) - temario.indexOf(b.t),
    )

export const tituloDe = (f: Figura) => f.title ?? `Figura ${f.orden} · ${f.tipo.toLowerCase()}`
