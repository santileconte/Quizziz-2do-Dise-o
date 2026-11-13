import { questions, historicas } from '../cuestionarios'
import { quizziz, enQuizziz } from '../cuestionarios/quizziz'
import { diagrams } from '../lib/diagrams'
import { puntua, type Question } from '../lib/quiz'
import { findMindMap } from '../mapas'
import { bloques, prioridadLabel, temario, type Tema } from '../temario'

const de = (t: Tema) => questions.filter((q) => t.temas.includes(q.tema))
const cuenta = (qs: Question[], pred: (q: Question) => boolean) => qs.filter(pred).length
const esParcial = (q: Question) => q.id.startsWith('p24')
const esRecu = (q: Question) => q.id.startsWith('r24')

/** Registros de la carpeta «Preguntas de Parcial y cuestionarios de practica semanal» y cómo se usó cada uno. */
const REGISTROS: { archivo: string; tipo: string; detalle: string; n: () => number | string }[] = [
  {
    archivo: 'Segundo Parcial Teoria 2024.docx',
    tipo: 'Parcial real',
    detalle: '9 capturas de la revisión de Moodle con las 16 consignas y sus claves. Transcripción literal.',
    n: () => cuenta(questions, esParcial),
  },
  {
    archivo: '2do recu parcial Teoria 2024.docx',
    tipo: 'Recuperatorio real',
    detalle: '22 capturas de celular con las 16 consignas y sus claves. El documento avisa que «algunos temas son del parcial pasado».',
    n: () => cuenta(questions, esRecu),
  },
  {
    archivo: 'Copia de Simulación Parcial 2 (IE3)_ Revisión del intento (1).pdf',
    tipo: 'Simulacro de la cátedra · intento A',
    detalle: 'Revisión de un intento de la simulación del aula virtual (24/11/2024). «Copia de» es solo el nombre del archivo.',
    n: () => cuenta(questions, (q) => q.id.startsWith('simA')),
  },
  {
    archivo: 'Copia de Simulación Parcial 2 ndfvjsnvk (IE3)_ Revisión del intento (1).pdf',
    tipo: 'Simulacro de la cátedra · intento B',
    detalle:
      'Otro intento de la misma simulación (23/11/2024), con 20 preguntas distintas: no es una copia del anterior. La pregunta 4 se conserva sin cambios como registro, pero se practica su versión del cuestionario 2026 (ver Decisiones tomadas).',
    n: () => `${cuenta(questions, (q) => q.id.startsWith('simB'))} preguntas + 1 conservada como registro`,
  },
  {
    archivo: 'Simulacro DSI (preguntas viejas y nuevas).html',
    tipo: 'Compilado hecho con IA · no suma evidencia',
    detalle:
      'Repite las dos simulaciones (no se cuentan otra vez), transcribe los cuestionarios semanales de 2026 y agrega 104 preguntas generadas. Es la única vía a los cuestionarios 2026: las capturas originales no están en la carpeta.',
    n: () => `${cuenta(questions, (q) => q.modalidad === 'cuestionario')} preguntas de cuestionarios + ${cuenta(questions, (q) => q.id.startsWith('ia-'))} generadas`,
  },
  {
    archivo: 'Simulacro_DSI_solo_material_base.pdf',
    tipo: 'Simulador de la cátedra · sin preguntas nuevas',
    detalle:
      'Las 94 preguntas de la cátedra del simulador: 35 de los cuestionarios 2026, 13 de las simulaciones 2024, las 19 figuras GoF y los 27 huecos de los diagramas del PUDS. Todas ya estaban en el banco: se cotejaron las claves (coinciden) y las figuras y los diagramas pasaron a figurar como material de la cátedra.',
    n: () => '94 cotejadas, 0 nuevas',
  },
  {
    archivo: 'Preguntas del Quizziz.pdf',
    tipo: 'Compilado de cuestionarios y parciales · copia',
    detalle: `75 capturas del Quizziz con la respuesta anotada a mano. ${75 - quizziz.length} ya estaban en el banco (parcial y recuperatorio 2024, simulaciones y cuestionarios 2026): no se cuentan otra vez y sus claves coinciden. Aportó ${quizziz.length} preguntas de cuestionarios que no están en otro registro, la figura del Cuestionario GRASP #4 y el texto de tres opciones que el compilado HTML había reconstruido.`,
    n: () => `${cuenta(questions, (q) => q.modalidad === 'quizziz')} nuevas + ${Object.values(enQuizziz).flat().length} anotadas`,
  },
  {
    archivo: 'Preguntas Patrones GOF.docx',
    tipo: 'Práctica de la cátedra',
    detalle: '19 figuras de ejemplos de patrones con su clave. El PDF del simulador las incluye entre las preguntas de la cátedra, con las mismas 19 claves.',
    n: () => cuenta(questions, (q) => q.id.startsWith('gof-')),
  },
  {
    archivo: 'preguntas de los diagramas.docx',
    tipo: 'Práctica de la cátedra · claves confirmadas por el usuario',
    detalle:
      'Las cinco figuras de los flujos del PUDS con huecos numerados y cinco opciones por hueco. No trae respuestas: las marcadas se dedujeron del libro (el PDF del simulador también las presenta como «clave deducida») y el usuario confirmó las 27.',
    n: () => cuenta(questions, (q) => q.id.startsWith('puds-')),
  },
  {
    archivo: 'preguntas multiple choice.docx',
    tipo: 'Generadas con IA',
    detalle: '30 preguntas y una «corrección» hechas con un chatbot. La clave es la de esa corrección, no de la cátedra.',
    n: () => cuenta(questions, (q) => q.id.startsWith('mc-')),
  },
  {
    archivo: 'quizzis (preguntas de cuest y parciales).docx',
    tipo: 'Enlace al Quizziz',
    detalle: 'Solo contiene el enlace al Quizziz (Wayground). Su contenido llegó aparte, en «Preguntas del Quizziz.pdf».',
    n: () => 0,
  },
]

/** Decisiones que cerraron pendientes. */
const DECISIONES: { titulo: string; texto: string; ids?: string }[] = [
  {
    titulo: 'Jerarquía para resolver claves contradictorias',
    texto:
      'Parcial o recuperatorio real, después cuestionario oficial y después simulación o compilado. Dentro de una misma categoría manda la versión más reciente. Una copia en el Quizziz no es una confirmación independiente.',
  },
  ...historicas.map((h) => ({
    titulo: `Caja blanca y caja negra · ${h.id} se practica como ${h.por}`,
    texto: `${h.motivo} Se practica y se corrige la versión 2026: las correctas son la de caja negra y «Un componente de prueba automatiza uno o varios procedimientos de prueba o partes de ellos». La versión 2024 se conserva sin cambios en su archivo y la diferencia queda en la nota de la pregunta.`,
    ids: `${h.por} (se practica) · ${h.id} (registro)`,
  })),
  {
    titulo: 'Diagramas de los flujos del PUDS',
    texto: 'El usuario confirmó las 27 claves. Se corrigen solas y suman puntaje; la confirmación figura en la corrección de cada una.',
    ids: Array.from({ length: 27 }, (_, i) => `puds-${String(i + 1).padStart(2, '0')}`).join(' · '),
  },
  {
    titulo: 'Quizziz, pregunta 67 (flujos de trabajo del PU)',
    texto:
      'Se mantiene como correcta «El flujo de trabajo de diseño suele tener más actividad durante la fase de elaboración», que es la adecuada entre las cuatro. La explicación aclara que, según Jacobson, Booch y Rumbaugh (§9.2, pág. 207, figura 9.2), el diseño es el centro de atención al final de Elaboración y al comienzo de Construcción.',
    ids: 'qz-67',
  },
  {
    titulo: 'Quizziz, preguntas 12, 45, 56, 65 y 67',
    texto: 'Provienen de cuestionarios. Se practican con la clave del Quizziz y corrección automática.',
    ids: 'qz-12 · qz-45 · qz-56 · qz-65 · qz-67',
  },
]

/** Notas sobre el material que no dependen de una pregunta puntual. */
const NOTAS: string[] = [
  'Cuestionarios semanales 2026: el texto viene de la transcripción del compilado HTML, que normalizó puntuación y mayúsculas. El Quizziz permitió cotejar los que repite (mismas claves) y recuperar las opciones que faltaban en GRASP #2 y Fases #2.',
  'Clasificación GoF: la tabla de la pág. 132 del apunte de Celina deja Flyweight en la columna de comportamiento. Acá figura como estructural de objeto, como en el índice del libro.',
  'Selección múltiple: el puntaje imita las revisiones de 2024 (cada correcta suma, cada incorrecta resta lo mismo, mínimo cero). El peso exacto de la resta se dedujo de dos capturas.',
  'Bloque B6 (Calidad y SQA): se dio el 12/11 y el cuadro lo deja sujeto al aviso del aula. Bloque B7 (interfaz, GUI, UX, diseño estructurado y Warnier): se tomó en 2024 y no está en las diapositivas de 2026.',
]

export function Temario() {
  const confirmados = temario.filter((t) => t.prio !== 'Pend' && t.prio !== 'Cond')
  const conReal = temario.filter((t) => de(t).some((q) => q.modalidad === 'parcial') && t.prio !== 'Pend')
  const dudosas = questions.filter((q) => !puntua(q))
  const reconstruidas = questions.filter((q) => q.recon)

  return (
    <main className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">Sección 05 — Qué entra y de dónde sale</p>
          <h1 className="display">
            Temario<span className="accent-dot">.</span>
          </h1>
          <p className="lede">
            Los temas en el orden de las clases de 2026, con la prioridad de cada uno, dónde leerlo y qué se tomó. La base es el
            cuadro de estudio; las prioridades se contrastaron con las notas de clase y con los registros de 2024.
          </p>
        </div>
      </section>

      <section className="stats">
        <div className="stat">
          <span className="stat-value">{confirmados.length}</span>
          <span className="stat-label">temas confirmados por las diapositivas</span>
        </div>
        <div className="stat">
          <span className="stat-value">{conReal.length}</span>
          <span className="stat-label">con consignas reales de 2024</span>
        </div>
        <div className="stat">
          <span className="stat-value">{dudosas.length}</span>
          <span className="stat-label">claves pendientes de verificación</span>
        </div>
      </section>

      <section className="tm-legend">
        <p>
          <span className="prio prio-A">A</span> muy probable · <span className="prio prio-B">B</span> probable ·{' '}
          <span className="prio prio-C">C</span> alcanza con reconocerlo · <span className="prio prio-Cond">Cond.</span> condicional ·{' '}
          <span className="prio prio-Pend">Sin conf.</span> sin confirmar
        </p>
        <p className="muted small">
          Evidencia: «real» cuenta las consignas del parcial (P) y del recuperatorio (R) de 2024; «cátedra» suma la simulación 2024, los
          cuestionarios 2026, el Quizziz y las figuras y diagramas del simulador. Una pregunta que aparece en dos registros se cuenta una sola vez, y el material de práctica no cuenta.
          Fuentes: Celina, Copia y Fidanza son los tres apuntes; PF, las diapositivas con notas de clase; Word, el apunte de la cátedra.
        </p>
      </section>

      {bloques.map((b) => {
        const items = temario.filter((t) => t.bloque === b.key)
        return (
          <section key={b.key} className="group">
            <div className="section-head">
              <h2 className="h2">
                <span className="unit">{b.unit}</span> {b.name}
              </h2>
              <span className="muted small">{b.aviso ?? `${items.length} temas`}</span>
            </div>
            <ol className="tm-list">
              {items.map((t) => (
                <Fila key={t.n} t={t} />
              ))}
            </ol>
          </section>
        )
      })}

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Registros analizados</h2>
          <span className="muted small">Qué es cada archivo de preguntas y cuántas aportó</span>
        </div>
        <ul className="tm-list">
          {REGISTROS.map((r) => (
            <li key={r.archivo} className="tm-item">
              <div className="tm-main">
                <p className="tm-title">{r.archivo}</p>
                <p className="muted small">{r.detalle}</p>
              </div>
              <div className="tm-side small">
                <span className="tag">{r.tipo}</span>
                <span className="muted">{typeof r.n() === 'number' ? `${r.n()} preguntas` : r.n()}</span>
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Pendientes de verificación</h2>
          <span className="muted small">No suman puntaje hasta que su id figure en src/cuestionarios/verificadas.ts</span>
        </div>
        <ul className="tm-list">
          {dudosas.length === 0 && (
            <li className="tm-item">
              <div className="tm-main">
                <p className="small">No quedan claves pendientes: todas las preguntas suman al puntaje.</p>
              </div>
            </li>
          )}
          {agrupar(dudosas).map(([motivo, qs]) => (
            <li key={motivo} className="tm-item">
              <div className="tm-main">
                <p className="tm-title">Clave sin verificar · {qs.length === 1 ? qs[0].src : `${qs.length} preguntas`}</p>
                <p className="muted small">{motivo[0].toUpperCase() + motivo.slice(1)}</p>
                <p className="small tm-ids">{qs.map((q) => q.id).join(' · ')}</p>
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Decisiones tomadas</h2>
          <span className="muted small">Pendientes cerrados</span>
        </div>
        <ul className="tm-list">
          {DECISIONES.map((d) => (
            <li key={d.titulo} className="tm-item">
              <div className="tm-main">
                <p className="tm-title">{d.titulo}</p>
                <p className="muted small">{d.texto}</p>
                {d.ids && <p className="small tm-ids">{d.ids}</p>}
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Limitaciones del material</h2>
          <span className="muted small">Texto reconstruido que no se puede cotejar: queda marcado</span>
        </div>
        <ul className="tm-list">
          {reconstruidas.map((q) => (
            <li key={q.id} className="tm-item">
              <div className="tm-main">
                <p className="tm-title">Texto reconstruido · {q.src}</p>
                <p className="muted small">
                  {q.recon![0].toUpperCase() + q.recon!.slice(1)} {puntua(q) ? q.nota?.match(/Se puntúa:.*$/)?.[0] ?? '' : 'No suma puntaje.'}
                </p>
                <p className="small tm-ids">{q.id}</p>
              </div>
            </li>
          ))}
          {NOTAS.map((d) => (
            <li key={d} className="tm-item">
              <div className="tm-main">
                <p className="small">{d}</p>
              </div>
            </li>
          ))}
        </ul>
      </section>
    </main>
  )
}

/** Junta las preguntas que comparten el mismo motivo de duda (salvo la referencia entre paréntesis). */
function agrupar(qs: Question[]) {
  const m = new Map<string, Question[]>()
  for (const q of qs) {
    const k = q.dud!.replace(/\s*\([^)]*\)\.?$/, '.')
    m.set(k, [...(m.get(k) ?? []), q])
  }
  return [...m]
}

function Fila({ t }: { t: Tema }) {
  const qs = de(t)
  const p = cuenta(qs, esParcial)
  const r = cuenta(qs, esRecu)
  const cat = cuenta(qs, (q) => ['simulacro', 'cuestionario', 'quizziz', 'practica'].includes(q.modalidad))
  const practica = qs.length - p - r - cat
  const mapa = t.mapa ? findMindMap(t.mapa) : undefined
  const graficos = (t.graficos ?? []).map((id) => diagrams.find((d) => d.id === id)).filter((d) => !!d)
  const corto = t.prio === 'Cond' ? 'Cond.' : t.prio === 'Pend' ? 'Sin conf.' : t.prio

  return (
    <li className="tm-item">
      <span className="index">{t.n}</span>
      <div className="tm-main">
        <p className="tm-title">
          <span className={`prio prio-${t.prio}`} title={prioridadLabel[t.prio]}>
            {corto}
          </span>{' '}
          {t.titulo}
          {t.cuadro !== t.prio && <span className="muted small"> · en el cuadro: {t.cuadro}</span>}
        </p>
        <p className="small">{t.fijar}</p>
        {t.nota && <p className="small tm-nota">{t.nota}</p>}
        <p className="muted small">
          Clase: {t.clase} · Apunte: {t.apunte} · PF: {t.pf}
          {t.word ? ` · Word: ${t.word}` : ''}
          {t.libro ? ` · Libro: ${t.libro}` : ''}
        </p>
      </div>
      <div className="tm-side small">
        <span className={p + r > 0 ? 'tm-real' : 'muted'}>
          {p + r > 0 ? `Real 2024: ${[p ? `${p} P` : '', r ? `${r} R` : ''].filter(Boolean).join(' + ')}` : 'Sin consignas reales'}
        </span>
        <span className="muted">
          Cátedra: {cat} · Práctica: {practica}
        </span>
        <span className="tm-links">
          {mapa && (
            <a className="link-quiet" href={`#/mapas/${mapa.id}`}>
              Mapa
            </a>
          )}
          {graficos.map((d, i) => (
            <a key={d!.id} className="link-quiet" href={`#/g/${d!.id}`} title={d!.title}>
              Gráfico{graficos.length > 1 ? ` ${i + 1}` : ''}
            </a>
          ))}
        </span>
      </div>
    </li>
  )
}
