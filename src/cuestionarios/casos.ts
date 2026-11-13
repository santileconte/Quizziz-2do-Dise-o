import { casosGenerados } from './casos-generados'

export interface Caso {
  titulo: string
  texto: string
}

// Textos que acompañan a un enunciado. Se muestran arriba de la pregunta.
export const casos: Record<string, Caso> = {
  // Segundo Parcial Teoria 2024.docx, Pregunta 13. Transcripción literal de la captura.
  eclipse: {
    titulo: 'Ejemplo del enunciado',
    texto:
      'Eclipse es un entorno de desarrollo integrado (IDE) que utiliza un sistema básico para la gestión del entorno. Este sistema proporciona servicios básicos como el manejo de recursos, la gestión de proyectos y la interfaz de usuario. Las funcionalidades adicionales, como soporte para lenguajes de programación (Java, Python, C++), se pueden instalar posteriormente como componentes separados para ampliar la funcionalidad ya existente. Los desarrolladores pueden personalizar o ampliar Eclipse sin modificar el sistema central.',
  },
  ...casosGenerados,
}
