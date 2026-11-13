import type { Caso } from './casos'

// Textos citados en enunciados del simulacro HTML.
export const casosGenerados: Record<string, Caso> = {
  "cita-01-03": {
    "titulo": "Texto citado",
    "texto": "LSP) The Liskov Substitution Principle.\n\nA program that uses an interface must not be confused by an implementation of that interface.\n\nPeople (including me) have made the mistake that this is about inheritance. It is not. It is about sub-typing. All implementations of interfaces are subtypes of an interface. All duck-types are subtypes of an implied interface. And, every user of the base interface, whether declared or implied, must agree on the meaning of that interface. If an implementation confuses the user of the base type, then if/switch statements will proliferate.\n\nThis principle is about keeping abstractions crisp and well-defined. It is impossible to believe that this is an outmoded concept.\n\nDan's slides are entirely correct on this topic; he simply missed the point of the principle. Simple code is code that maintains crisp subtype relationships."
  }
}
