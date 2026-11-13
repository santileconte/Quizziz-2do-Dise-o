/**
 * Estado de verificación de las claves.
 *
 * Mientras una pregunta tenga el campo `dud`, se puede responder y ver la clave propuesta, pero no suma al puntaje
 * ni al progreso. Cuando se confirma la clave, su id va en `verificadas` con quién y cómo la confirmó: pasa a
 * corregirse sola y en la corrección se muestra esa nota. Si la clave propuesta estaba mal, corregí además el campo
 * `a` en el archivo de la pregunta.
 *
 * Los ids se ven en la pantalla «Temario».
 */

const PUDS =
  'Clave confirmada por el usuario (13/11/2026). El documento original no trae respuestas: la marcada se dedujo del flujo del libro.'

export const verificadas: Record<string, string> = Object.fromEntries(
  Array.from({ length: 27 }, (_, i) => [`puds-${String(i + 1).padStart(2, '0')}`, PUDS]),
)

/**
 * Preguntas cuya clave contradice a otra versión de mayor jerarquía. Se conserva su texto en el archivo de origen,
 * sin tocar, pero no se practica: se practica la versión indicada en `por`, que lleva la diferencia en su nota.
 *
 * Jerarquía para resolver contradicciones entre claves: parcial o recuperatorio real > cuestionario oficial >
 * simulación o compilado. Dentro de una misma categoría manda la versión más reciente. Una copia en el Quizziz no
 * confirma nada por sí sola.
 */
export const reemplazadas: Record<string, { por: string; motivo: string }> = {
  'simB-04': {
    por: 'cq-06-02',
    motivo:
      'La clave de la Simulación B (2024) marca «Los casos de prueba de caja blanca se derivan de los casos de uso». El Cuestionario Diseño, Implementación y Prueba #2 (2026), de mayor jerarquía, y la teoría dicen que de los casos de uso salen los de caja negra.',
  },
}
