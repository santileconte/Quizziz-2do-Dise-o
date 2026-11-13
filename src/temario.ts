import type { UnitKey } from './lib/quiz'

// Temario del segundo parcial. Sigue el orden de las clases de 2026 (según las diapositivas con notas, «PF»)
// y toma como base el «Cuadro de estudio». Las fuentes citan archivo y página:
//   Celina = «Apunte Segundo Parcial - Celina.pdf» · Copia = «Copia de Apunte Diseño.pdf»
//   Fidanza = «ApunteDiseñoSistemasInformación.pdf» · PF = «PF_Powers_de_Clase_364p.pdf»
//   WM = «WM_Microservicios_del_Word.pdf» (págs. 130–153 del Word de la cátedra)

export const bloques: { key: UnitKey; unit: string; name: string; aviso?: string }[] = [
  { key: 'b1', unit: 'B1', name: 'Diseño orientado a objetos' },
  { key: 'b2', unit: 'B2', name: 'Arquitectura de software y sistemas distribuidos' },
  { key: 'b3', unit: 'B3', name: 'Proceso Unificado (PUDS)' },
  { key: 'b4', unit: 'B4', name: 'Patrones GoF' },
  { key: 'b5', unit: 'B5', name: 'Agilidad y XP' },
  { key: 'b6', unit: 'B6', name: 'Calidad', aviso: 'Condicional: se dio en clase el 12/11, falta confirmar si entra.' },
  {
    key: 'b7',
    unit: 'B7',
    name: 'Temas de 2024 sin confirmar',
    aviso: 'Interfaz, GUI, UX, diseño estructurado y Warnier: se tomaron en 2024 y no están en las diapositivas de 2026.',
  },
]

/** A: muy probable · B: probable · C: alcanza con reconocerlo · Cond: condicional · Pend: sin confirmar. */
export type Prioridad = 'A' | 'B' | 'C' | 'Cond' | 'Pend'

export const prioridadLabel: Record<Prioridad, string> = {
  A: 'Prioridad A',
  B: 'Prioridad B',
  C: 'Prioridad C',
  Cond: 'Condicional',
  Pend: 'Sin confirmar',
}

export interface Tema {
  n: string
  bloque: UnitKey
  titulo: string
  /** Prioridad de este repaso y la que proponía el cuadro de estudio. */
  prio: Prioridad
  cuadro: Prioridad
  /** Por qué cambió la prioridad o qué dijo el profesor, con su fuente. */
  nota?: string
  fijar: string
  /** Fecha de la clase según las diapositivas con notas. */
  clase: string
  apunte: string
  pf: string
  word?: string
  libro?: string
  /** Nombres de tema que usan las preguntas de Cuestionarios. */
  temas: string[]
  mapa?: string
  graficos?: string[]
}

export const temario: Tema[] = [
  { n: '01', bloque: 'b1', titulo: 'SOLID', prio: 'B', cuadro: 'B', fijar: 'Reconocer qué principio se viola y qué cambio lo corrige.', clase: '13/08', apunte: 'Celina 5–8', pf: '1–7', word: '1–8', libro: 'Carmona 7–23', temas: ['SOLID'], mapa: 'b1-solid', graficos: ['b1-01-solid'] },
  { n: '02', bloque: 'b1', titulo: 'Máquina de estados', prio: 'C', cuadro: 'C', fijar: 'Estado, evento, guarda y acción.', clase: '13/08 (práctica)', apunte: 'Fidanza 46–52', pf: '8–11', temas: ['Máquina de estados'], mapa: 'b1-estados', graficos: ['b1-03-maquina-de-estados'] },
  { n: '03', bloque: 'b1', titulo: 'GRASP', prio: 'B', cuadro: 'B', fijar: 'Asignar responsabilidades y justificar cohesión y acoplamiento.', clase: '20/08', apunte: 'Celina 8–17', pf: '12–22', word: '9–22', libro: 'Larman 444–445', temas: ['GRASP'], mapa: 'b1-grasp', graficos: ['b1-02-grasp'] },
  { n: '04', bloque: 'b1', titulo: 'Estados compuestos', prio: 'C', cuadro: 'C', fijar: 'Leer subestados y transiciones en el ejemplo.', clase: '20/08 (práctica)', apunte: 'Fidanza 49–52', pf: '23–25', temas: ['Estados compuestos'], mapa: 'b1-estados', graficos: ['b1-03-maquina-de-estados'] },

  { n: '05', bloque: 'b2', titulo: 'Decisiones y vistas 4+1', prio: 'B', cuadro: 'B', nota: 'Sobre elegir la arquitectura según el requisito no funcional clave, la nota de clase dice «esta es una de las preguntas más importantes» (PF, pág. 30).', fijar: 'Qué decide el arquitecto y qué muestra cada vista 4+1.', clase: '03/09', apunte: 'Celina 38–43', pf: '26–34', word: '23–27 y 77–82', libro: 'Sommerville 2016, 172–175', temas: ['Decisiones y vistas 4+1'], mapa: 'b2-disarq', graficos: ['b2-05-vistas-4mas1'] },
  { n: '06', bloque: 'b2', titulo: 'Qué es arquitectura', prio: 'A', cuadro: 'A', nota: '«Arquitectura es un tema central para la materia […]. Va a preguntar mucho en el parcial» (PF, pág. 113).', fijar: 'Definición, niveles e importancia de las decisiones.', clase: '03/09', apunte: 'Celina 17–24', pf: '35–38', word: '29–34', libro: 'Bass 16–20 y 44–48', temas: ['Qué es arquitectura'], mapa: 'b2-arq' },
  { n: '07', bloque: 'b2', titulo: 'Estructuras', prio: 'A', cuadro: 'A', fijar: 'Distinguir módulos, componentes/conectores y asignación.', clase: '03/09', apunte: 'Celina 20–22', pf: '39–44', word: '30–45', libro: 'Bass 21–37', temas: ['Estructuras (Bass)'], mapa: 'b2-arq', graficos: ['b2-01-estructuras'] },
  { n: '08', bloque: 'b2', titulo: 'Escenarios de calidad', prio: 'A', cuadro: 'A', fijar: 'Reconstruir las seis partes de un escenario.', clase: '03/09', apunte: 'Celina 24–29', pf: '45–50', word: '46–53', libro: 'Bass 65, fig. 3.1', temas: ['Atributos y escenarios de calidad'], mapa: 'b2-escenarios', graficos: ['b2-02-escenario-calidad'] },
  { n: '09', bloque: 'b2', titulo: 'Modificabilidad', prio: 'A', cuadro: 'A', nota: 'De los atributos de calidad, «hay dos que nos vamos a enfocar, va a ser los que va a tomar» (PF, pág. 49): modificabilidad y rendimiento.', fijar: 'Identificar el cambio, su costo y la táctica aplicable.', clase: '03/09', apunte: 'Celina 30–35', pf: '51–60', word: '54–67', libro: 'Bass 159–161', temas: ['Modificabilidad'], mapa: 'b2-modif', graficos: ['b2-03-tacticas-modificabilidad'] },
  { n: '10', bloque: 'b2', titulo: 'Rendimiento', prio: 'A', cuadro: 'B', nota: 'Sube de B a A: es uno de los dos atributos que el profesor dijo que va a tomar (PF, pág. 49). No aparece en los registros de 2024.', fijar: 'Separar control de la demanda de gestión de recursos.', clase: '03/09', apunte: 'Celina 35–38', pf: '61–68', word: '68–75', libro: 'Bass 177 y 183', temas: ['Rendimiento'], mapa: 'b2-perf', graficos: ['b2-04-tacticas-rendimiento'] },
  { n: '11', bloque: 'b2', titulo: 'Capas', prio: 'A', cuadro: 'A', fijar: 'Identificar responsabilidades y dependencias entre capas.', clase: '03/09', apunte: 'Celina 43–46', pf: '69–74', word: '84–87', libro: 'Sommerville 2016, 178–180', temas: ['Capas', 'Estilos arquitectónicos (comparación)'], mapa: 'b2-estilos', graficos: ['b2-06-capas'] },
  { n: '12', bloque: 'b2', titulo: 'Repositorio y cliente-servidor', prio: 'A', cuadro: 'A', fijar: 'Reconocer depósito central y prestación de servicios.', clase: '03/09', apunte: 'Celina 46–48', pf: '75–77', word: '88–91', libro: 'Sommerville 2016, 181 y 183', temas: ['Repositorio y cliente-servidor'], mapa: 'b2-estilos' },
  { n: '13', bloque: 'b2', titulo: 'Tuberías, filtros y microkernel', prio: 'A', cuadro: 'A', fijar: 'Reconocer cadena de transformaciones y núcleo con plug-ins.', clase: '03/09', apunte: 'Celina 48–49 · Copia 152–153', pf: '78–85', word: '92–100', libro: 'Sommerville 2016, 183–184', temas: ['Tuberías, filtros y microkernel'], mapa: 'b2-estilos' },
  { n: '14', bloque: 'b2', titulo: 'Distribución', prio: 'A', cuadro: 'A', fijar: 'Explicar ventajas, escalabilidad, heterogeneidad y dificultades.', clase: '03/09', apunte: 'Celina 50–53', pf: '86–91', word: '101–105', libro: 'Sommerville 2016, 493–499', temas: ['Sistemas distribuidos'], mapa: 'b2-dist' },
  { n: '15', bloque: 'b2', titulo: 'Topologías distribuidas', prio: 'A', cuadro: 'A', fijar: 'Distinguir maestro-esclavo, cliente liviano/pesado, multinivel, middleware y P2P.', clase: '03/09 y 17/09', apunte: 'Celina 53–58', pf: '92–105', word: '106–124', libro: 'Sommerville 2016, 500–513', temas: ['Topologías distribuidas'], mapa: 'b2-topo', graficos: ['b2-09-patrones-distribuidos'] },
  { n: '16', bloque: 'b2', titulo: 'SOA', prio: 'B', cuadro: 'B', fijar: 'Seguir proveedor, registro y solicitante. Asociar los estándares con su función.', clase: '17/09', apunte: 'Celina 58–60', pf: '106–109', word: '126–129', libro: 'Sommerville 2016, 526, fig. 18.2', temas: ['SOA'], mapa: 'b2-soa', graficos: ['b2-07-soa'] },
  { n: '17', bloque: 'b2', titulo: 'Microservicios', prio: 'A', cuadro: 'A', nota: 'El profesor pidió investigar más este tema y recomendó el artículo de Fowler (PF, pág. 113).', fijar: 'Reconocer la topología y explicar fronteras, datos por servicio, gateway y coordinación.', clase: '17/09', apunte: 'Celina 60–61 · Copia 169', pf: '110–113', word: '130–153 (WM)', libro: 'Sommerville 2020, 169–174 y 179–182', temas: ['Microservicios'], mapa: 'b2-micro', graficos: ['b2-08-microservicios'] },
  { n: '18', bloque: 'b2', titulo: 'SaaS', prio: 'C', cuadro: 'C', nota: '«Gaona no hizo hincapié en SAAS en clase» (PF, pág. 114).', fijar: 'Distinguir modelo de entrega de estilo arquitectónico.', clase: '17/09', apunte: '—', pf: '114', word: '155–156', libro: 'Sommerville 2016, 513–517', temas: ['SaaS'], mapa: 'b2-soa' },

  { n: '19', bloque: 'b3', titulo: 'Visión general', prio: 'A', cuadro: 'A', fijar: 'Dirigido por casos de uso, centrado en arquitectura, iterativo e incremental.', clase: '24/09', apunte: 'Celina 62–64 · Copia 207 (4P + H)', pf: '115–126', word: '157–168', libro: 'PUDS 29–34', temas: ['PUDS: visión general'], mapa: 'b3-puds' },
  { n: '20', bloque: 'b3', titulo: 'Ciclo y conceptos', prio: 'A', cuadro: 'A', nota: 'Sobre el gráfico del ciclo de vida: «Diagrama muy importante, resume prácticamente todo» (PF, pág. 130).', fijar: 'Leer la intensidad de cada disciplina y distinguir fase, iteración, trabajador, actividad y artefacto.', clase: '24/09', apunte: 'Celina 64–65 y 73', pf: '127–140', word: '169–180', libro: 'PUDS 37 y 124', temas: ['PUDS: ciclo y conceptos'], mapa: 'b3-ciclo', graficos: ['b3-06-ciclo-de-vida'] },
  { n: '21', bloque: 'b3', titulo: 'Fases e hitos', prio: 'A', cuadro: 'A', fijar: 'Poder decir objetivo, hito y entregable de cada fase.', clase: '01/10', apunte: 'Celina 65–67', pf: '141–146', word: '183–189', libro: 'PUDS 36–38, 362–363, 384, 397 y 410', temas: ['PUDS: fases e hitos'], mapa: 'b3-fases', graficos: ['b3-06-ciclo-de-vida'] },
  { n: '22', bloque: 'b3', titulo: 'Requisitos y contexto', prio: 'A', cuadro: 'A', fijar: 'Distinguir lista de características, modelo de dominio, modelo de negocio y casos de uso del sistema.', clase: '01/10', apunte: 'Celina 67–73 · Copia 211–214', pf: '147–159', word: '190–201', libro: 'PUDS 144–145 y 160–161', temas: ['Requisitos y contexto'], mapa: 'b3-req' },
  { n: '23', bloque: 'b3', titulo: 'Flujo de Requisitos', prio: 'A', cuadro: 'A', nota: 'Completar la figura fue la Pregunta 3 del parcial 2024.', fijar: 'Dibujar los cuatro trabajadores y las cinco actividades.', clase: '01/10', apunte: 'Celina 73–80, figura 75', pf: '160–166 y 252', word: '202–207, figura 290', libro: 'PUDS 159, fig. 7.10', temas: ['Flujo de Requisitos'], mapa: 'b3-freq', graficos: ['b3-01-flujo-requisitos'] },
  { n: '24', bloque: 'b3', titulo: 'Realización de CU y CRC', prio: 'B', cuadro: 'B', fijar: 'Pasar de responsabilidades a clases y dibujar la interacción del caso.', clase: '01/10 (práctica)', apunte: 'Fidanza 39–46', pf: '167–175', word: '215–216 y 230–231', temas: ['Realización de CU y CRC'], mapa: 'b3-freq' },
  { n: '25', bloque: 'b3', titulo: 'Modelo de Análisis', prio: 'A', cuadro: 'A', fijar: 'Reconocer entidad, control y frontera. Explicar qué es una realización de análisis.', clase: '08/10', apunte: 'Celina 81–87', pf: '176–185', word: '208–219', libro: 'PUDS 187–208', temas: ['Modelo de Análisis'], mapa: 'b3-man', graficos: ['b3-07-modelos', 'b3-08-analisis-vs-diseno'] },
  { n: '26', bloque: 'b3', titulo: 'Flujo de Análisis', prio: 'A', cuadro: 'A', fijar: 'Asociar arquitectura, caso de uso, clase y paquete con su trabajador.', clase: '08/10', apunte: 'Celina 87–92, figura 88', pf: '186–191 y 256', word: '219–224, figura 294', libro: 'PUDS 209, fig. 8.18', temas: ['Flujo de Análisis'], mapa: 'b3-fan', graficos: ['b3-02-flujo-analisis'] },
  { n: '27', bloque: 'b3', titulo: 'Modelo de Diseño', prio: 'A', cuadro: 'A', fijar: 'Compararlo con Análisis. Ubicar clases, interfaces, subsistemas, despliegue y realización de diseño.', clase: '08/10', apunte: 'Celina 93–99', pf: '192–203', word: '225–236', libro: 'PUDS 227–242', temas: ['Modelo de Diseño'], mapa: 'b3-mdis', graficos: ['b3-07-modelos', 'b3-08-analisis-vs-diseno'] },
  { n: '28', bloque: 'b3', titulo: 'Flujo de Diseño', prio: 'A', cuadro: 'A', nota: 'Completar la figura fue una consigna del recuperatorio 2024.', fijar: 'Reconstruir arquitectura, caso de uso, clase y subsistema con sus flechas.', clase: '08/10', apunte: 'Celina 99–107, figura 100', pf: '204–213 y 261', word: '237–249, figura 299', libro: 'PUDS 243, fig. 9.16', temas: ['Flujo de Diseño'], mapa: 'b3-fdis', graficos: ['b3-03-flujo-diseno'] },
  { n: '29', bloque: 'b3', titulo: 'Implementación', prio: 'A', cuadro: 'A', fijar: 'Ubicar componente, build, integrador y prueba unitaria.', clase: '15/10', apunte: 'Celina 107–118, figura 113', pf: '214–229 y 266', word: '251–267, figura 304', libro: 'PUDS 288–292', temas: ['Implementación'], mapa: 'b3-impl', graficos: ['b3-04-flujo-implementacion'] },
  { n: '30', bloque: 'b3', titulo: 'Prueba', prio: 'A', cuadro: 'A', fijar: 'Distinguir roles, artefactos y trazas de caja negra y blanca. Separar planificar de diseñar la prueba.', clase: '15/10', apunte: 'Celina 118–127, flujo en 123', pf: '230–247 y 270', word: '268–284', libro: 'PUDS 304 y 308–312', temas: ['Prueba'], mapa: 'b3-prueba', graficos: ['b3-05-flujo-prueba'] },
  { n: '31', bloque: 'b3', titulo: 'Repaso de los cinco flujos', prio: 'A', cuadro: 'B', nota: 'Sube de B a A: las responsabilidades de un trabajador «a lo largo del PUDS» se preguntaron en el parcial (ingeniero de componentes) y en el recuperatorio (ingeniero de casos de uso) de 2024.', fijar: 'Comparar entradas, salidas y responsables con las figuras cerradas.', clase: 'repaso', apunte: 'Celina 75, 88, 100, 113 y 123', pf: '249–285', word: '288–311', temas: ['Repaso de los cinco flujos'], mapa: 'b3-repaso', graficos: ['b3-01-flujo-requisitos', 'b3-02-flujo-analisis', 'b3-03-flujo-diseno', 'b3-04-flujo-implementacion', 'b3-05-flujo-prueba'] },

  { n: '32', bloque: 'b4', titulo: 'Definición, formato y clasificación', prio: 'A', cuadro: 'A', nota: '«Es importante saber explicar y aplicar los patrones que se ven en las clases» (PF, pág. 295).', fijar: 'Separar propósito y alcance. Reconocer intención, aplicabilidad, estructura y consecuencias.', clase: '22/10', apunte: 'Celina 127–132', pf: '286–295', word: '324–332', libro: 'GoF 12–19', temas: ['GoF: definición, formato y clasificación', 'Otros patrones del catálogo'], mapa: 'b4-gof', graficos: ['b4-01-clasificacion-gof'] },
  { n: '33', bloque: 'b4', titulo: 'Factory Method', prio: 'A', cuadro: 'A', fijar: 'Identificar producto, creador y método redefinido.', clase: '22/10', apunte: 'Celina 133–134', pf: '296–299', word: '333–336', libro: 'GoF 210–212', temas: ['Factory Method'], mapa: 'b4-creac', graficos: ['b4-02-factory-method'] },
  { n: '34', bloque: 'b4', titulo: 'Singleton', prio: 'B', cuadro: 'B', fijar: 'Ubicar la instancia única y el acceso a ella.', clase: '22/10', apunte: 'Celina 134–135', pf: '299', word: '337', libro: 'GoF 307–308', temas: ['Singleton'], mapa: 'b4-creac' },
  { n: '35', bloque: 'b4', titulo: 'Adapter', prio: 'A', cuadro: 'A', nota: '«Adapter estaba en dos clasificaciones distintas, por lo cual es importante su estudio» (PF, pág. 295).', fijar: 'Reconocer interfaz esperada, adaptada y variante de clase u objeto.', clase: '22/10', apunte: 'Celina 136–137', pf: '300–301', word: '338–340', libro: 'GoF 133–135', temas: ['Adapter'], mapa: 'b4-estruc', graficos: ['b4-04-adapter'] },
  { n: '36', bloque: 'b4', titulo: 'Observer', prio: 'A', cuadro: 'A', fijar: 'Seguir suscripción, cambio de estado y notificación.', clase: '22/10', apunte: 'Celina 143–144', pf: '302–303', word: '340–341', libro: 'GoF 278–280', temas: ['Observer'], mapa: 'b4-comport', graficos: ['b4-06-observer'] },
  { n: '37', bloque: 'b4', titulo: 'Abstract Factory', prio: 'A', cuadro: 'A', fijar: 'Reconocer familias de productos y distinguirlas de Factory Method.', clase: '29/10', apunte: 'Celina 135–136', pf: '305–307', word: '343–345', libro: 'GoF 124–126', temas: ['Abstract Factory'], mapa: 'b4-creac', graficos: ['b4-03-abstract-factory'] },
  { n: '38', bloque: 'b4', titulo: 'Strategy', prio: 'A', cuadro: 'A', fijar: 'Identificar contexto y algoritmos intercambiables. Comparar con State.', clase: '29/10', apunte: 'Copia 198–200', pf: '308–309', word: '346', libro: 'GoF 323–325', temas: ['Strategy'], mapa: 'b4-comport', graficos: ['b4-07-strategy'] },
  { n: '39', bloque: 'b4', titulo: 'Composite', prio: 'B', cuadro: 'B', fijar: 'Identificar componente, hoja y compuesto en un árbol.', clase: '29/10', apunte: 'Celina 138–139', pf: '310–312', word: '347–348', libro: 'GoF 182–184', temas: ['Composite'], mapa: 'b4-estruc', graficos: ['b4-05-composite'] },
  { n: '40', bloque: 'b4', titulo: 'Facade, Proxy, State e Iterator', prio: 'A', cuadro: 'A', nota: 'Tres consignas reales en 2024: State sobre código y Fachada en el parcial, Proxy en el recuperatorio.', fijar: 'Reconocer sus estructuras y explicar qué problema resuelve cada uno. Practicar State sobre código.', clase: 'guía de estudio', apunte: 'Celina 139–145', pf: '286–295', word: '332', libro: 'GoF 203, 246, 298–299 y 315', temas: ['Facade, Proxy, State e Iterator'], mapa: 'b4-estruc', graficos: ['b4-08-state', 'b4-09-proxy'] },

  { n: '41', bloque: 'b5', titulo: 'Agilidad y Manifiesto', prio: 'A', cuadro: 'B', nota: 'Sube de B a A: los valores y principios del Manifiesto se preguntaron en el parcial y en el recuperatorio de 2024.', fijar: 'Diferenciar valores, principios y enfoques predictivos/adaptativos.', clase: '05/11', apunte: 'Celina 145–149', pf: '313–328', word: '349–366', temas: ['Agilidad y Manifiesto'], mapa: 'b5-agil', graficos: ['b5-01-manifiesto-valores'] },
  { n: '42', bloque: 'b5', titulo: 'XP', prio: 'A', cuadro: 'A', nota: '«Gaona dice que nos enfoquemos en las prácticas centrales»: metáfora, diseño simple, refactorización y estándares de codificación, y ver qué son los spikes (PF, pág. 342).', fijar: 'Recorrer historia → plan → iteración → pruebas → entrega. Fijar diseño simple, spike, TDD y refactoring.', clase: '05/11', apunte: 'Celina 149–157, gráfico 153', pf: '329–342', word: '367–380', libro: 'Beck 24–30', temas: ['XP'], mapa: 'b5-xp', graficos: ['b5-02-proyecto-xp', 'b5-03-xp-listas'] },
  { n: '43', bloque: 'b5', titulo: 'Agile Modeling y postagilismo', prio: 'C', cuadro: 'C', fijar: 'Reconocer el objetivo del modelado ágil y ubicar el gráfico.', clase: '05/11', apunte: '—', pf: '343–344', word: '380–381', temas: ['Agile Modeling y postagilismo'], mapa: 'b5-agil' },

  { n: '44', bloque: 'b6', titulo: 'Calidad y costos', prio: 'Cond', cuadro: 'Cond', fijar: 'Comparar calidad de diseño y conformidad, perspectivas y costos de calidad.', clase: '12/11', apunte: 'Copia 235–238', pf: '345–355', word: '382–392', libro: 'Pressman 343–357', temas: ['Calidad y costos'], mapa: 'b6-calidad', graficos: ['b6-01-costos-de-calidad'] },
  { n: '45', bloque: 'b6', titulo: 'Revisiones y SQA', prio: 'Cond', cuadro: 'Cond', fijar: 'Diferenciar revisión, control y aseguramiento. Ubicar tareas y métricas de SQA.', clase: '12/11', apunte: 'Copia 238–241', pf: '355–364', word: '393–405', libro: 'Pressman 358–388', temas: ['Revisiones y SQA'], mapa: 'b6-sqa' },

  { n: 'P1', bloque: 'b7', titulo: 'Interfaz, entradas/salidas, GUI y UX', prio: 'Pend', cuadro: 'Pend', nota: 'En 2024: 3 consignas del parcial y 2 del recuperatorio. No figura en las diapositivas de 2026.', fijar: 'Solo si la cátedra lo confirma.', clase: 'sin clase en 2026', apunte: 'Copia 11–39 (ventana modal, 28) · Fidanza 199–215', pf: '—', temas: ['Interfaz, GUI y UX'] },
  { n: 'P2', bloque: 'b7', titulo: 'Diseño Estructurado y Warnier', prio: 'Pend', cuadro: 'Pend', nota: 'En 2024: 1 consigna del parcial y 2 del recuperatorio. Un compañero anotó en el recuperatorio «esto creo que no entra». No figura en las diapositivas de 2026.', fijar: 'Solo si la cátedra lo confirma.', clase: 'sin clase en 2026', apunte: 'Fidanza 216–222 (notación 219, fan-in y fan-out 222)', pf: '—', temas: ['Diseño estructurado y Warnier'] },
]

/** Orden del temario para listar los temas de las preguntas. */
const orden = new Map(temario.flatMap((t, i) => t.temas.map((x, k) => [x, i * 10 + k] as const)))
export const ordenTema = (tema: string) => orden.get(tema) ?? 9999
export const temaDe = (tema: string) => temario.find((t) => t.temas.includes(tema))
