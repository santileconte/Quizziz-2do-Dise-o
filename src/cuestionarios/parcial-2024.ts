import type { ItemDef, UnitKey } from '../lib/quiz'

// Segundo Parcial de Teoría 2024 (IE3). Transcripción literal de las 9 capturas de la revisión de Moodle
// incluidas en «Segundo Parcial Teoria 2024.docx». Las claves son las que muestra Moodle («La respuesta correcta es»).
// No se corrigió ortografía ni puntuación.
const F = 'Segundo Parcial Teoria 2024.docx'
const src = (img: number | string, p: number) => `${F} · imagen ${img} · Pregunta ${p}`

export const parcial2024: (ItemDef & { unit: UnitKey })[] = [
  {
    unit: 'b7',
    t: 'mc',
    tema: 'Interfaz, GUI y UX',
    src: src(1, 1),
    q: '¿Cuál/es de las siguientes opciones describe mejor la categoría de manipulación directa de fuerza media (o distancia traslacional media)?',
    o: [
      'Interactuar con el espacio virtual tocando, moviendo o agarrando objetos en una representación en pantalla táctil.',
      'Controlar acciones virtuales con gestos corporales, como movimientos de manos, pies o cabeza.',
      'Usar gafas de realidad virtual para entrar al espacio virtual, donde el usuario puede caminar o volar mientras el escenario cambia con sus movimientos.',
      'Utilizar un ratón o joystick para realizar acciones en un espacio virtual mediante una función de mapeo.',
    ],
    a: 0,
    ref: 'Tema sin confirmar para este año. Copia de Apunte Diseño, págs. 11–39.',
  },
  {
    unit: 'b4',
    t: 'multi',
    tema: 'Facade, Proxy, State e Iterator',
    src: src('2–3', 2),
    q: 'Dado el siguiente código en C# que representa un sistema básico de autenticación. Si se le aplicara el patrón State, ¿cuáles de las siguientes afirmaciones serían correctas?',
    code: `class UserAccount
{
    public string AccountState { get; private set; }

    public UserAccount()
    {
        AccountState = "Active"; // El estado inicial es "Activo".
    }

    public void Login()
    {
        if (AccountState == "Active")
        {
            Console.WriteLine("Login successful!");
        }
        else if (AccountState == "Suspended")
        {
            Console.WriteLine("Account is suspended. Cannot log in.");
        }
        else if (AccountState == "Deactivated")
        {
            Console.WriteLine("Account is deactivated. Cannot log in.");
        }
    }

    public void SuspendAccount()
    {
        if (AccountState == "Active")
        {
            AccountState = "Suspended";
            Console.WriteLine("Account suspended.");
        }
        else
        {
            Console.WriteLine("Cannot suspend account. Current state: " + AccountSta…
        }
    }

    public void ReactivateAccount()
    {
        if (AccountState == "Suspended")
        {
            AccountState = "Active";
            Console.WriteLine("Account reactivated.");
        }
        else if (AccountState == "Deactivated")
        {
            Console.WriteLine("Cannot reactivate a deactivated account.");
        }
        else
        {
            Console.WriteLine("Account is already active.");
        }
    }

    public void DeactivateAccount()
    {
        if (AccountState != "Deactivated")
        {
            AccountState = "Deactivated";
            Console.WriteLine("Account deactivated.");
        }
        else
        {
            Console.WriteLine("Account is already deactivated.");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        UserAccount account = new UserAccount();

        account.Login(); // Activo, permite el login
        account.SuspendAccount(); // Suspende la cuenta
        account.Login(); // No permite el login (suspendida)
        […]`,
    o: [
      'Cada estado se encapsularía en su propia clase, lo que facilitaría agregar nuevos estados sin modificar el código existente.',
      'Se crearía una subclase para cada método existente en UserAccount que desencadena un cambio de estado (Login, SuppendAccount, ReactivateAccount, DeactivateAccount)',
      'UserAccount seguiría siendo responsable de definir cómo se comportan los estados específicos.',
      'UserAccount adoptaría el rol de la clase Cliente en el patrón.',
      'Las transiciones de estado se realizarían directamente en el objeto UserAccount, eliminando la necesidad de clases adicionales.',
      'Se evitaría que el comportamiento de los estados esté disperso a lo largo de múltiples métodos, centralizando la lógica en las clases de estado.',
    ],
    a: [0, 5],
    e: 'Con State, UserAccount pasa a ser el Contexto: delega en un objeto estado y cada ConcreteState concentra el comportamiento de ese estado. Se crea una clase por estado (Active, Suspended, Deactivated), no una por método.',
    nota: 'La captura corta el código: una línea se sale del margen («AccountSta…») y el final de Main no se ve; esas partes están marcadas con «…» y no se completaron. En la opción b se lee «SuppendAccount»; la imagen tiene baja resolución.',
    ref: 'Celina, págs. 142–143. GoF, fig. p. 315.',
  },
  {
    unit: 'b3',
    t: 'rel',
    tema: 'Flujo de Requisitos',
    src: src(4, 3),
    q: 'En el contexto del PUDS, complete el flujo de trabajo de Requisitos indicando trabajadores y actividades',
    img: ['p24-03-flujo-requisitos.png'],
    i: [
      ['[1]', 'Analista de Sistemas'],
      ['[2]', 'Arquitecto'],
      ['[3]', 'Diseñador de Interfaz de usuario'],
      ['[4]', 'Encontrar actores y casos de uso'],
      ['[5]', 'Priorizar casos de uso'],
      ['[6]', 'Detallar casos de uso'],
      ['[7]', 'Prototipar interfaz de usuario'],
    ],
    e: 'Es la figura 7.10 del PUDS: el analista encuentra actores y casos de uso y estructura el modelo; el arquitecto prioriza; el especificador detalla; el diseñador de interfaz prototipa.',
    nota: 'En el parcial cada número tenía un desplegable. La captura solo muestra la opción elegida, así que acá las opciones son las siete respuestas correctas.',
    ref: 'Celina, págs. 73–80 (figura en 75). PF, págs. 160–166 y 252.',
  },
  {
    unit: 'b5',
    t: 'multi',
    tema: 'Agilidad y Manifiesto',
    src: src(5, 4),
    q: '¿Cuál/es de los siguientes enunciados representan valores/principios del Manifiesto Ágil?',
    o: [
      'El éxito del proyecto se mide principalmente por la puntualidad en la entrega del software.',
      'La colaboración con el cliente es más importante que la negociación contractual.',
      'Los planes iniciales deben ser seguidos estrictamente para evitar cambios en el alcance.',
      'El trabajo de los desarrolladores debe ser supervisado constantemente para garantizar la calidad',
      'Se prioriza la entrega frecuente de software funcional, incluso en iteraciones cortas',
    ],
    a: [1, 4],
    e: 'Valor 3: colaboración del cliente por sobre negociación contractual. Principio 3: entregar software funcionando frecuentemente.',
    ref: 'Celina, págs. 146–147.',
  },
  {
    unit: 'b3',
    t: 'multi',
    tema: 'Repaso de los cinco flujos',
    src: src(5, 5),
    q: 'Marque las responsabilidades de un ingeniero de componentes a lo largo del PUDS',
    o: [
      'Es responsable de la integridad del modelo de pruebas, asegurándose de que el modelo cumpla su propósito.',
      'Es responsable de la integridad de una o varias realizaciones de casos de uso, asegurándose de que cumplan con los requisitos establecidos en ellas.',
      'Es responsable de definir y mantener las operaciones, métodos, atributos, relaciones y requisitos de implementación de una o varias clases de diseño.',
      'Es responsable de definir y mantener el código fuente de uno o varios componentes de archivo, asegurándose de que cada componente implemente la funcionalidad correcta.',
    ],
    a: [2, 3],
    e: 'La a describe al ingeniero de pruebas y la b al ingeniero de casos de uso. El ingeniero de componentes define clases en análisis y diseño, y en implementación mantiene el código de los componentes y hace la prueba de unidad.',
    ref: 'Celina, págs. 87, 99 y 112.',
  },
  {
    unit: 'b4',
    t: 'multi',
    tema: 'GoF: definición, formato y clasificación',
    src: src(6, 6),
    q: '¿Cuál/es de los siguientes patrones de diseño pertenece a la categoría De Comportamiento y tiene un alcance de Clase?',
    o: ['Factory Method', 'Iterator', 'Decorator', 'Template Method', 'Interpreter'],
    a: [3, 4],
    e: 'De comportamiento con alcance de clase solo hay dos: Interpreter y Template Method. Factory Method es de clase pero creacional.',
    ref: 'Celina, pág. 132.',
  },
  {
    unit: 'b7',
    t: 'mc',
    tema: 'Diseño estructurado y Warnier',
    src: src('6–7', 7),
    q: '¿Cuál es la relación ideal entre el alcance de control y el alcance de efecto en el diseño estructurado?',
    o: [
      'El alcance de control debe ser mayor que el alcance de efecto.',
      'El alcance de control debe estar contenido dentro del alcance de efecto.',
      'El alcance de efecto debe ser siempre mayor que el alcance de control.',
      'El alcance de efecto y el alcance de control son inversamente proporcionales.',
      'El alcance de efecto debe estar contenido dentro del alcance de control.',
    ],
    a: 4,
    ref: 'Tema sin confirmar para este año. Apunte de Fidanza, págs. 216–222.',
  },
  {
    unit: 'b7',
    t: 'mc',
    tema: 'Interfaz, GUI y UX',
    src: src(7, 8),
    q: '¿Cuál es un ejemplo de sesgo introducido al establecer límites para los valores reportados?',
    o: [
      'Mostrar primero los resultados de ciertas aerolíneas en un sistema de reservas.',
      'Crear gráficos con colores llamativos para resaltar ciertos datos específicos.',
      'Elaborar un informe que incluya cuentas con solo una semana de atraso en los pagos.',
      'Ordenar los datos alfabéticamente, destacando ciertos elementos.',
    ],
    a: 2,
    ref: 'Tema sin confirmar para este año. Copia de Apunte Diseño, págs. 11–39.',
  },
  {
    unit: 'b2',
    t: 'multi',
    tema: 'Estructuras (Bass)',
    src: src(8, 9),
    q: '¿Cuáles de las siguientes preguntas pertenecen principalmente a las estructuras de asignación (allocation) dentro de una arquitectura de software? (Bass et al.)',
    o: [
      '¿Qué otros elementos de software puede utilizar un módulo?',
      '¿Qué módulos están relacionados con otros módulos por relaciones de generalización o especialización (herencia)?',
      '¿En qué procesador(es) se ejecuta cada elemento del software?',
      '¿Cuáles son los principales componentes ejecutables y cómo interactúan en tiempo de ejecución?',
      '¿En qué directorios o archivos se almacena cada elemento durante el desarrollo, pruebas y construcción del sistema?',
    ],
    a: [2, 4],
    e: 'Asignación relaciona el software con lo que no es software: hardware (despliegue), archivos (implementación) y equipos (asignación de trabajo). La a y la b son de módulos; la d, de componentes y conectores.',
    ref: 'Celina, págs. 20–22. PF, págs. 39–44.',
  },
  {
    unit: 'b3',
    t: 'multi',
    tema: 'PUDS: fases e hitos',
    src: src('8–9', 10),
    q: '¿Cuál/es de las siguientes actividades generales corresponden a la fase de inicio del PUDS?',
    o: [
      'Prepara una oferta completa que cubre el cronograma, el personal necesario y el costo dentro de los límites establecidos por las prácticas comerciales.',
      'Captura casos de uso hasta aproximadamente el 80% de los requisitos funcionales-',
      'Crea una línea base de la arquitectura.',
      'Demostrar a los potenciales usuarios o clientes que el sistema propuesto es capaz de resolver su problema.',
      'Delimitar el alcance del sistema propuesto.',
    ],
    a: [3, 4],
    e: 'Inicio delimita el alcance y muestra que el sistema es viable. Capturar cerca del 80% de los casos de uso, crear la línea base de la arquitectura y preparar la oferta completa corresponden a elaboración.',
    ref: 'Celina, págs. 65–67. PF, págs. 141–146.',
  },
  {
    unit: 'b5',
    t: 'multi',
    tema: 'XP',
    src: src(9, 11),
    q: '¿Cuál/es de las siguientes NO SON consideradas actividades de XP?',
    o: ['Codificar', 'Analizar', 'Diseñar', 'Probar', 'Planificar', 'Escuchar'],
    a: [1, 4],
    e: 'Las cuatro actividades básicas de XP son programar (codificar), probar, escuchar y diseñar.',
    ref: 'Celina, pág. 151. PF, pág. 332.',
  },
  {
    unit: 'b3',
    t: 'multi',
    tema: 'Modelo de Diseño',
    src: src(10, 12),
    q: 'Marque las afirmaciones verdaderas acerca de la Realización de Casos de Uso-Diseño según el PUDS',
    o: [
      'Una clase de diseño es exclusiva de una realización de casos de uso - diseño',
      'En un diagrama de secuencia podríamos incluir los subsistemas participantes',
      'Puede tener una traza directa con el modelo de casos de uso, en el caso de que no exista modelo de análisis',
      'El flujo de eventos-diseño es una descripción textual que complementa a los diagramas de interacción, pero no debe llegar al detalle de incluir objetos.',
    ],
    a: [2, 1],
    e: 'Una clase de diseño puede participar en varias realizaciones. El flujo de sucesos-diseño explica los diagramas en términos de objetos o subsistemas que interactúan.',
    ref: 'Celina, págs. 96 y 102–104.',
  },
  {
    unit: 'b2',
    t: 'mc',
    tema: 'Tuberías, filtros y microkernel',
    src: src('10–11', 13),
    ctx: 'eclipse',
    q: 'Dado el siguiente ejemplo, determine qué tipo de estilo arquitectónico que utiliza',
    o: ['Microkernel', 'Cliente-Servidor', 'Componentes distribuidos', 'En Capas', 'Sistema central y componentes extendidos'],
    a: 0,
    e: 'Un núcleo con las funciones básicas y plug-ins que se agregan sin modificarlo: microkernel o plug-in.',
    ref: 'Celina, págs. 48–49. PF, págs. 82–85.',
  },
  {
    unit: 'b3',
    t: 'multi',
    tema: 'PUDS: visión general',
    src: src(11, 14),
    q: '¿Cuál/es son las características que hacen al PUDS centrado en la arquitectura?',
    o: [
      'La arquitectura se empieza a desarrollar desde la fase de inicio en forma de boceto de la arquitectura',
      'Es centrado en la arquitectura porque los casos de uso, una vez implementados, deben encajar en la arquitectura y a su vez, los casos de uso guían el desarrollo de la arquitectura.',
      'El enfoque centrado en la arquitectura disminuye la necesidad de revisiones posteriores a su diseño inicial.',
      'Es centrado en la arquitectura ya que su descripción contiene una vista detallada de todo el sistema',
    ],
    a: [1, 0],
    e: 'La arquitectura es una vista del diseño completo con lo más importante, sin los detalles, y madura junto con los casos de uso.',
    ref: 'Celina, págs. 62–63 y 65.',
  },
  {
    unit: 'b7',
    t: 'mc',
    tema: 'Interfaz, GUI y UX',
    src: src(12, 15),
    q: 'Clasifique la siguiente ventana emergente de acuerdo a su modalidad, en este caso no se puede hacer nada más en el SO hasta que se brinde una respuesta.',
    img: ['p24-15-ventana.png'],
    o: ['Modal Heterogénea', 'Modal de Aplicación', 'No Modal de Aplicación', 'No Modal Heterogénea', 'No Modal de Sistema', 'Modal de Sistema'],
    a: 5,
    ref: 'Tema sin confirmar para este año. Copia de Apunte Diseño, pág. 28.',
  },
  {
    unit: 'b4',
    t: 'multi',
    tema: 'Facade, Proxy, State e Iterator',
    src: src(12, 16),
    q: '¿Cuál/es de las siguientes se consideran situaciones en las que se podría aplicar el patrón Fachada?',
    o: [
      'Desea evitar un enlace permanente entre una abstracción y su implementación.',
      'Desea proporcionar una interfaz simple a un subsistema complejo.',
      'Desea crear una clase reutilizable que coopere con clases no relacionadas o imprevistas, es decir, clases que no necesariamente tienen interfaces compatibles.',
      'Desea crear capas de subsistemas.',
      'Desea añadir responsabilidades a objetos individuales de forma dinámica y transparente, es decir, sin afectar a otros objetos.',
    ],
    a: [1, 3],
    e: 'La a es aplicabilidad de Bridge, la c de Adapter y la e de Decorator.',
    ref: 'Celina, págs. 139–140.',
  },
]
