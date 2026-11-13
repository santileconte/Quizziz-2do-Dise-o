import type { ItemDef, Modalidad, Question, UnitKey } from '../lib/quiz'
import { parcial2024 } from './parcial-2024'
import { recuperatorio2024 } from './recuperatorio-2024'
import { simulacroCatedra } from './simulacro-catedra'
import { cuestionariosCatedra } from './cuestionarios-catedra'
import { practicaFigurasGof } from './practica-figuras-gof'
import { practicaDiagramasPuds } from './practica-diagramas-puds'
import { practicaMultipleChoice } from './practica-multiple-choice'
import { practicaSimulacroIa } from './practica-simulacro-ia'
import { propias } from './propias'
import { quizziz, enQuizziz } from './quizziz'
import { verificadas, reemplazadas } from './verificadas'
import { bloques } from '../temario'

export { casos } from './casos'

export const quizUnits = bloques

type Cruda = ItemDef & { unit: UnitKey; id?: string }

/** Las preguntas con clave en duda dejan de estarlo cuando su id figura en `verificadas.ts`. */
const armar = (modalidad: Modalidad, prefijo: string, items: Cruda[]): Question[] =>
  items.map((item, i) => {
    const id = item.id ?? `${prefijo}-${String(i + 1).padStart(2, '0')}`
    const q = { ...item, id, modalidad } as Question
    const qz = enQuizziz[id]
    if (qz) q.src = `${q.src ?? ''} · también en el Quizziz (${qz.length > 1 ? 'preguntas' : 'pregunta'} ${qz.join(', ')} de 75)`
    if (q.dud && verificadas[id]) {
      delete q.dud
      q.verif = verificadas[id]
    }
    return q
  })

// Cada pregunta figura una sola vez. Las que se repiten entre la Simulación 2024 y los cuestionarios 2026
// quedan en la Simulación, con la otra aparición anotada en su fuente.
const todas: Question[] = [
  ...armar('parcial', 'p24', parcial2024),
  ...armar('parcial', 'r24', recuperatorio2024),
  ...armar('simulacro', 'sim', simulacroCatedra),
  ...armar('cuestionario', 'cq', cuestionariosCatedra),
  ...armar('quizziz', 'qz', quizziz),
  ...armar('practica', 'gof', practicaFigurasGof),
  ...armar('practica', 'puds', practicaDiagramasPuds),
  ...armar('ia', 'mc', practicaMultipleChoice),
  ...armar('ia', 'ia', practicaSimulacroIa),
  ...armar('propia', 'n', propias),
]

/** Versiones reemplazadas por otra de mayor jerarquía (ver `verificadas.ts`): se conservan como registro, no se practican. */
export const historicas: (Question & { por: string; motivo: string })[] = todas
  .filter((q) => reemplazadas[q.id])
  .map((q) => ({ ...q, ...reemplazadas[q.id] }))

export const questions: Question[] = todas.filter((q) => !reemplazadas[q.id])

const porId = new Map(questions.map((q) => [q.id, q]))
export const findQuestion = (id: string) => porId.get(id)

const figuras = import.meta.glob('./img/*.{png,jpg,jpeg,webp}', { eager: true, query: '?url', import: 'default' }) as Record<string, string>

/** URL de una figura de `src/cuestionarios/img/`. */
export const figura = (file: string) => figuras[`./img/${file}`]
