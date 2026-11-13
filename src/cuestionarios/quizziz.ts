import type { ItemDef, UnitKey } from '../lib/quiz'

// «Preguntas del Quizziz.pdf»: 75 capturas del Quizziz (Wayground) que figura como enlace en
// «quizzis (preguntas de cuest y parciales).docx», con la respuesta anotada a mano debajo de cada una.
// Todas son de selección múltiple («Seleccione todas las opciones correctas»).
//
// 70 de las 75 ya están en el banco: se cuentan una sola vez y su aparición en el Quizziz queda anotada
// en la fuente (mapa `enQuizziz`). Acá van solo las 5 que no figuran en ningún otro registro. Según el usuario,
// las cinco provienen de cuestionarios; sus claves son las del Quizziz.
// Transcripción literal de las capturas: no se corrigió ortografía ni puntuación.

const F = 'Preguntas del Quizziz.pdf'
const src = (pag: number, n: number) => `${F} · pág. ${pag} · pregunta ${n}/75 · proviene de un cuestionario`

export const quizziz: (ItemDef & { unit: UnitKey; id: string })[] = [
  {
    id: 'qz-12',
    unit: 'b1',
    t: 'multi',
    tema: 'SOLID',
    src: src(4, 12),
    q: '¿Qué principio SOLID incumple el siguiente código?',
    code: `public class Vehicle {

    public int getWheelCount() {
        return 4;
    }

    public int getMaxSpeed() {
        return 200;
    }

    @Override
    public String toString() {
        return "wheelCount=" + getWheelCount() + ", maxSpeed=" + getMaxSpeed();
    }

    public void print() {
        System.out.println(toString());
    }
}`,
    o: ['Responsabilidad Única', 'Segregación de Interfaces', 'Sustitución de Liskov', 'Alta Cohesión'],
    a: [0],
    e: 'La clase representa los datos del vehículo y además se encarga de imprimirlos por consola: tiene más de una razón para cambiar. Alta Cohesión no es un principio SOLID.',
    nota: 'Variante del Cuestionario SOLID #4 (cq-01-04): el mismo enunciado con otra clase Vehicle y cuatro opciones. Se incluye aparte porque el código y las opciones son distintos.',
    ref: 'Celina, pág. 6.',
  },
  {
    id: 'qz-45',
    unit: 'b1',
    t: 'multi',
    tema: 'SOLID',
    src: src(19, 45),
    q: `Dado el siguiente párrafo de un libro, seleccione los principios involucrados.
"La importancia de este principio se vuelve obvia cuando consideras las consecuencias de violarlo. Supongamos que tenemos una función f que toma, como su argumento, un puntero o referencia a alguna clase base B. Supongamos que también existe algún derivado D de B que, cuando se pasa a f en la apariencia de B, causa que f se comporte incorrectamente. Entonces, D viola el ___. Claramente, D es frágil en presencia de f.
Los autores de f se verán tentados a poner algún tipo de prueba para D, de manera que f pueda comportarse correctamente cuando se le pase un D. Esta prueba viola el ___ porque ahora d no está cerrada a todos los diversos derivados de B.`,
    o: ['LSP - OCP', 'OCP - SRP', 'OCP- LSP', 'LSP - LSP', 'SRP - OCP'],
    a: [0],
    e: 'El primer hueco es LSP: el derivado D no puede usarse donde se espera la clase base B sin que f falle. El segundo es OCP: agregar a f una prueba por el tipo D obliga a modificarla cada vez que aparece un derivado nuevo, así que f deja de estar cerrada a la modificación.',
    nota: 'El texto dice «ahora d no está cerrada»; se refiere a la función f. Se conserva como está en la captura.',
    ref: 'Celina, págs. 6–7.',
  },
  {
    id: 'qz-56',
    unit: 'b3',
    t: 'multi',
    tema: 'Implementación',
    src: src(22, 56),
    q: '¿Qué describe un plan de compilación (build) de integración?',
    o: [
      'Una lista de los subsistemas y componentes necesarios para implementar la funcionalidad esperada por la compilación',
      'Una lista de las clases necesarias para implementar la funcionalidad esperada por la compilación',
      'Una lista de casos de uso y/o escenarios que será implementados en la compilación',
      'Describe la secuencia de compilaciones necesarias para una integración',
    ],
    a: [0, 2, 3],
    e: 'El plan de integración de construcciones describe la secuencia de construcciones y, para cada una, la funcionalidad esperada (casos de uso o escenarios) y las partes del modelo de implementación afectadas (subsistemas y componentes). No se expresa en clases, que son del modelo de diseño.',
    ref: 'Celina, págs. 111–112.',
  },
  {
    id: 'qz-65',
    unit: 'b2',
    t: 'multi',
    tema: 'Atributos y escenarios de calidad',
    src: src(26, 65),
    q: '¿Cuál de las siguientes opciones relaciona correctamente un atributo de calidad con el objetivo principal que busca asegurar en un sistema de software?',
    o: [
      'Escalabilidad (Escalability): permitir que el sistema se integre fácilmente con otros',
      'Seguridad (Security): garantizar que el sistema no cause daños físicos',
      'Deployability (Desplegabilidad): facilitar la liberación rápida y confiable de nuevas versiones',
      'Usability (Usabilidad): asegurar tiempos de respuesta adecuados y throughput alto',
    ],
    a: [2],
    e: 'Integrarse con otros sistemas es interoperabilidad; no causar daños físicos es safety, no security; los tiempos de respuesta y el throughput son rendimiento. La desplegabilidad es uno de los atributos que afectan al proceso de construcción y evolución.',
    nota: 'La opción a dice «Escalability»; se conserva como está en la captura.',
    ref: 'Celina, pág. 25.',
  },
  {
    id: 'qz-67',
    unit: 'b3',
    t: 'multi',
    tema: 'PUDS: ciclo y conceptos',
    src: src(26, 67),
    q: '¿Cuál de las siguientes afirmaciones sobre los flujos de trabajo en el Proceso Unificado es correcta?',
    o: [
      'El flujo de trabajo de implementación comienza solo después de que todos los requisitos estén completamente definidos',
      'El flujo de trabajo de prueba solo se realiza en la fase de transición',
      'El flujo de trabajo de diseño suele tener más actividad durante la fase de elaboración',
      'Los flujos de trabajo no se pueden superponer',
    ],
    a: [2],
    e: 'Según Jacobson, Booch y Rumbaugh, el diseño es el centro de atención al final de Elaboración y al comienzo de Construcción. Después, el énfasis se desplaza hacia la implementación. Los flujos de trabajo se superponen y se repiten en las iteraciones.\nPor eso las otras tres son falsas: la implementación empieza antes de tener todos los requisitos, la prueba se hace en todas las fases y los flujos sí se superponen. Entre las cuatro opciones, es la afirmación adecuada.',
    ref: 'Jacobson, Booch y Rumbaugh, El Proceso Unificado de Desarrollo de Software, §9.2, pág. 207 (figura 9.2). Celina, págs. 64–65.',
  },
]

/**
 * Preguntas del banco que también están en el Quizziz, con su número (de 75). No suman como evidencia:
 * el Quizziz es una copia. Las consignas de completar figuras (p24-03, r24-06) y la de emparejar (simA-01)
 * aparecen allí partidas en una pregunta por hueco; las claves de cada hueco coinciden con las del banco.
 */
export const enQuizziz: Record<string, number[]> = {
  'r24-16': [1],
  'p24-03': [2, 18, 30, 38, 40, 59, 75],
  'simA-13': [3],
  'simB-17': [4],
  'r24-12': [5],
  'simA-01': [6, 10, 33, 35],
  'simA-02': [7],
  'simB-13': [8],
  'cq-02-02': [9],
  'simA-05': [11],
  'p24-04': [13],
  'p24-02': [14],
  'r24-14': [15],
  'simB-06': [16],
  'p24-06': [17],
  'r24-06': [19, 23, 24, 62, 74],
  'simB-10': [20],
  'r24-01': [21],
  'p24-13': [22],
  'simA-09': [25],
  'simA-17': [26],
  'r24-07': [27],
  'simA-15': [28],
  'r24-11': [29],
  'p24-05': [31],
  'simB-12': [32],
  'simA-18': [34],
  'simB-08': [36],
  'p24-16': [37],
  'p24-09': [39],
  'simA-20': [41],
  'cq-05-02': [42],
  'simB-03': [43],
  'simB-11': [44],
  'simB-04': [46],
  'simB-02': [47],
  'r24-08': [48],
  'r24-10': [49],
  'r24-04': [50],
  'r24-02': [51],
  'cq-05-07': [52],
  'simB-09': [53],
  'simA-11': [54],
  'p24-10': [55],
  'p24-14': [57],
  'simA-08': [58],
  'cq-02-04': [60],
  'simA-10': [61],
  'p24-12': [63],
  'simA-12': [64],
  'cq-01-01': [66],
  'p24-11': [68],
  'r24-03': [69],
  'simA-04': [70],
  'simB-05': [71],
  'cq-02-01': [72],
  'simB-07': [73],
}
