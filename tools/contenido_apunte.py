"""Apunte de estudio (src/mapas/apunte.json).

Cada sección: clave, bloque, título, fuente principal (con páginas), otras fuentes y bloques.
Un bloque es (tipo, texto[, etiqueta]). Tipos: p, li, h, callout, table (texto = filas).
Las etiquetas permiten que los mapas mentales citen un bloque: 'solid.srp'.
"""

SECCIONES = []


def S(clave, bloque, titulo, src, orig, bloques):
    SECCIONES.append(dict(clave=clave, unit=bloque, title=titulo, src=src, orig=orig, bloques=bloques))


# ═══════════════════════════ B1 · Diseño orientado a objetos
S('solid', 'b1', 'Principios SOLID', 'Celina, págs. 5–8', 'PF, págs. 1–7', [
    ('p', 'SOLID es un acrónimo de cinco principios de diseño orientado a objetos. No son nuevos: el aporte de **Robert C. Martin** fue reunirlos y darles nombre. Buscan código más fácil de entender, de probar y de cambiar, y están muy relacionados entre sí.', 'que'),
    ('li', '**S · Responsabilidad única (SRP).** Una clase debe tener **una sola razón para cambiar**. Busca clases cohesivas y evita que un cambio se propague. Señales de que se viola: la clase mezcla dos capas (por ejemplo, lógica de negocio y persistencia), tiene muchos métodos públicos, es difícil de probar, o un grupo de métodos usa la mitad de los atributos y otro grupo la otra mitad. El riesgo opuesto es terminar con muchas clases de una sola línea.', 'srp'),
    ('li', '**O · Abierto/Cerrado (OCP).** Una clase debe estar **abierta a la extensión y cerrada a la modificación**: se agrega comportamiento sin tocar código ya probado. La señal típica de incumplimiento es un `if/else` o `switch` por tipo que hay que editar cada vez que aparece un caso nuevo; se resuelve con polimorfismo. No conviene forzarlo antes de que surja la necesidad.', 'ocp'),
    ('li', '**L · Sustitución de Liskov (LSP).** Donde se espera el tipo base debe poder usarse **cualquier subtipo** sin que el programa se confunda. No trata solo de herencia: toda implementación de una interfaz debe respetar su **significado**, no solo su firma. Modelar copiando la realidad suele romperlo.', 'lsp'),
    ('li', '**I · Segregación de interfaces (ISP).** Los clientes **no deben depender de interfaces que no usan**. Una interfaz «gruesa» se divide en varias pequeñas y cohesivas.', 'isp'),
    ('li', '**D · Inversión de dependencias (DIP).** Los módulos de alto nivel no dependen de los de bajo nivel: **ambos dependen de abstracciones**. Así la lógica no queda atada a frameworks o a la base de datos y se puede probar aislada. Lo habitual es usar un inyector de dependencias.', 'dip'),
    ('callout', '**Ley de Deméter (mínimo conocimiento).** Un objeto solo habla con sus «amigos inmediatos»: él mismo, sus atributos, lo que crea y lo que recibe. Encadenar llamadas a objetos obtenidos de otros es una alarma de acoplamiento.', 'demeter'),
    ('callout', '**Cómo se pregunta.** En el cuestionario de la cátedra dan un fragmento de código y piden el principio que incumple: mirá si hay un `if` por tipo (OCP), una clase que calcula, guarda e imprime (SRP) o una interfaz con métodos que algún cliente no usa (ISP).', 'examen'),
])

S('estados', 'b1', 'Máquina de estados y estados compuestos', 'Apunte de Fidanza, págs. 46–52', 'PF, págs. 8–11 y 23–25 (práctica)', [
    ('p', 'La máquina de estados describe el **ciclo de vida de un objeto**: los estados por los que pasa y qué lo hace cambiar.', 'que'),
    ('li', '**Estado:** situación en la que el objeto cumple una condición, hace una actividad o espera un evento.', 'estado'),
    ('li', '**Transición:** paso de un estado a otro. Se rotula `evento [guarda] / acción`.', 'transicion'),
    ('li', '**Evento:** lo que dispara la transición. **Guarda:** condición que debe ser verdadera para que se dispare. **Acción:** lo que se ejecuta al dispararse.', 'partes'),
    ('li', '**Estado inicial** (círculo lleno) y **estado final** (círculo con borde).', 'inifin'),
    ('li', '**Transición automática:** no lleva evento; ocurre sola, por ejemplo al pasar un tiempo. No tiene notación propia y debe aclararse en el enunciado.', 'auto'),
    ('li', '**Estado compuesto:** contiene subestados. Una transición que sale del compuesto vale para cualquiera de sus subestados.', 'compuesto'),
    ('callout', 'Es un tema de práctica (prioridad C): alcanza con leer bien estado, evento, guarda y acción en un ejemplo.', 'nota'),
])

S('grasp', 'b1', 'Patrones GRASP', 'Celina, págs. 8–17', 'PF, págs. 12–22 · Larman, Applying UML and Patterns', [
    ('p', 'GRASP (*General Responsibility Assignment Software Patterns*) son nueve patrones para **asignar responsabilidades** a las clases. Una responsabilidad es lo que un objeto debe **conocer** y **hacer**. Creador, Experto y Controlador dicen a quién asignar; Bajo Acoplamiento y Alta Cohesión sirven para evaluar las alternativas; los otros cuatro contienen el impacto del cambio.', 'que'),
    ('table', [['Patrón', 'Problema', 'Solución'],
               ['Creador', '¿Quién crea una instancia de A?', 'B crea A si la contiene o agrega, la registra, la usa estrechamente o tiene los datos para inicializarla. En una relación todo-parte, el todo.'],
               ['Experto en información', '¿A quién asigno una responsabilidad?', 'A la clase que tiene la información necesaria para cumplirla.'],
               ['Bajo acoplamiento', '¿Cómo reduzco el impacto del cambio?', 'Asignar de modo que el acoplamiento se mantenga bajo.'],
               ['Controlador', '¿Quién recibe un evento del sistema detrás de la interfaz?', 'Un objeto que representa al sistema o al caso de uso; coordina y delega, no hace el trabajo.'],
               ['Alta cohesión', '¿Cómo mantengo clases manejables?', 'Asignar de modo que cada clase tenga responsabilidades relacionadas y no haga demasiado.'],
               ['Polimorfismo', '¿Cómo manejo alternativas según el tipo?', 'Con operaciones polimórficas, sin preguntar por el tipo.'],
               ['Fabricación pura', '¿Y si ninguna clase del dominio sirve?', 'Inventar una clase que no representa nada del dominio para sostener cohesión y acoplamiento.'],
               ['Indirección', '¿Cómo evito el acoplamiento directo?', 'Un objeto intermedio media entre los dos.'],
               ['Variaciones protegidas', '¿Cómo evito que una variación afecte a otros?', 'Envolver el punto de variación con una interfaz estable.']], 'tabla'),
    ('li', '**Acoplamiento:** cuán dependiente es una clase de otras. Es una medida subjetiva; la herencia también acopla. Bajo acoplamiento favorece el mantenimiento y la reutilización, pero acoplamiento cero no existe: sin colaboración no hay sistema.', 'acop'),
    ('li', '**Cohesión:** cuán relacionadas están las responsabilidades de una clase. Cohesión y acoplamiento son «yin y yang»: una mala cohesión suele traer mal acoplamiento.', 'cohe'),
    ('li', '**Controlador:** no se pone lógica de la aplicación en la interfaz. Un controlador que hace todo está «saturado» y pierde cohesión.', 'ctrl'),
    ('li', '**Fabricación pura, Indirección y Variaciones protegidas** suelen aparecer juntas: un adaptador es una indirección, puede ser una clase fabricada y protege al dominio de las variaciones de un proveedor externo. No son equivalentes.', 'combo'),
    ('callout', '**Cómo se pregunta.** Dan una situación y piden el patrón («ninguna clase natural puede asumir la responsabilidad» → Fabricación pura) o comparan el acoplamiento de dos diagramas de comunicación.', 'examen'),
])

# ═══════════════════════════ B2 · Arquitectura y sistemas distribuidos
S('disarq', 'b2', 'Diseño arquitectónico: decisiones y vistas 4+1', 'Celina, págs. 38–43', 'PF, págs. 26–34 · Sommerville (2016), págs. 172–175', [
    ('p', 'El diseño arquitectónico es la **primera etapa del diseño**: define cómo se organiza el sistema en componentes que se comunican. Viene después de la ingeniería de requisitos.', 'que'),
    ('li', 'Se puede mirar a **pequeña escala** (arquitectura de un programa) o a **gran escala** (sistemas empresariales distribuidos).', 'escala'),
    ('li', 'Documentar la arquitectura sirve para **comunicarse con los interesados**, **analizar el sistema** y **reutilizar a gran escala**.', 'ventajas'),
    ('h', 'El requisito no funcional crítico orienta la arquitectura'),
    ('table', [['Si lo crítico es…', 'conviene…'],
               ['Rendimiento', 'Concentrar las operaciones críticas en pocos componentes, en la misma computadora; componentes grandes.'],
               ['Seguridad (security)', 'Estructura en capas, con los activos más críticos en las capas internas.'],
               ['Protección (safety)', 'Operaciones relacionadas con la seguridad en un solo componente o en pocos.'],
               ['Disponibilidad', 'Componentes redundantes que se puedan reemplazar sin detener el sistema.'],
               ['Mantenibilidad', 'Componentes pequeños y autocontenidos, fáciles de cambiar.']], 'rnf'),
    ('p', 'Estos criterios chocan: componentes grandes mejoran el rendimiento y componentes pequeños la mantenibilidad. Se busca un compromiso, a veces con estilos distintos para distintas partes.', 'conflicto'),
    ('h', 'Vistas 4+1 (Kruchten)'),
    ('li', '**Vista lógica:** abstracciones clave como objetos y clases. Relaciona los requisitos con entidades.', 'logica'),
    ('li', '**Vista de procesos:** cómo se compone el sistema de procesos en tiempo de ejecución. Sirve para juzgar rendimiento y disponibilidad.', 'procesos'),
    ('li', '**Vista de desarrollo:** cómo se descompone el software para desarrollarlo (módulos, capas, librerías). Útil para programadores y gerentes.', 'desarrollo'),
    ('li', '**Vista física:** hardware y distribución de los componentes en los procesadores. Útil para planear el despliegue.', 'fisica'),
    ('li', '**+1 · Escenarios o casos de uso:** vinculan las cuatro vistas. Es la organización que usa el Proceso Unificado.', 'escenarios'),
])

S('arq', 'b2', 'Qué es la arquitectura de software', 'Celina, págs. 17–24', 'PF, págs. 35–38 · Bass et al., págs. 16–20 y 44–48', [
    ('p', 'La arquitectura de software de un sistema es el **conjunto de estructuras necesarias para razonar sobre él**: elementos de software, relaciones entre ellos y propiedades de ambos (Bass).', 'def'),
    ('li', '**Es una abstracción:** muestra lo que hace falta para entender el sistema y omite lo privado de cada elemento. Se concentra en las interfaces.', 'abstraccion'),
    ('li', '**Todo sistema tiene una arquitectura**, esté o no documentada, y **no todas son buenas**.', 'todo'),
    ('li', '**Incluye el comportamiento** de los elementos en la medida en que sirve para razonar.', 'comportamiento'),
    ('li', '**La arquitectura es diseño, pero no todo el diseño es arquitectura.** No se ocupa del diseño de cada clase.', 'diseno'),
    ('li', '**La definen los atributos de calidad**, no la funcionalidad: los requisitos funcionales no determinan la arquitectura, aunque esta debe soportarlos.', 'rnf'),
    ('li', 'Un patrón arquitectónico **no es lo mismo** que un patrón de diseño: trabaja a otra escala.', 'patron'),
    ('h', 'Niveles'),
    ('li', '**Arquitectura de software:** el nivel más específico; la parte lógica.', 'nsw'),
    ('li', '**Arquitectura de sistema:** suma el hardware, las redes y las personas.', 'nsis'),
    ('li', '**Arquitectura empresarial:** por encima de ambas; roles, procesos e información de toda la organización.', 'nemp'),
    ('h', 'Por qué importa'),
    ('li', 'Potencia o inhibe atributos de calidad, contiene las **decisiones de diseño tempranas y difíciles de cambiar**, mejora la comunicación entre interesados, permite razonar sobre el cambio, el costo y el calendario, y define restricciones de implementación.', 'importa'),
    ('callout', 'El profesor avisó que arquitectura es un tema central y que «va a preguntar mucho en el parcial».', 'enfasis'),
])

S('estructuras', 'b2', 'Estructuras: módulos, componentes y conectores, asignación', 'Celina, págs. 20–22', 'PF, págs. 39–44 · Bass et al., págs. 21–37', [
    ('p', 'Bass agrupa las estructuras en tres clases. No es obligatorio documentar las tres: se usan las que ayudan a razonar sobre un atributo que le importa a algún interesado.', 'que'),
    ('li', '**Estructuras de módulos (estáticas).** Los módulos son **unidades de implementación**: clases, paquetes, capas. Responden: ¿qué funcionalidad tiene cada módulo?, ¿qué otros elementos de software puede usar?, ¿qué módulos se relacionan por generalización o especialización? Ejemplos: descomposición, usos, capas, clases.', 'modulos'),
    ('li', '**Estructuras de componentes y conectores (C&C, dinámicas).** Muestran el sistema **en ejecución**: servicios, clientes, servidores, filtros, y los conectores por los que interactúan. Responden: ¿cuáles son los principales componentes ejecutables y cómo interactúan?, ¿qué partes pueden funcionar en paralelo?, ¿qué partes se replican? Son cruciales para rendimiento, seguridad y disponibilidad.', 'cyc'),
    ('li', '**Estructuras de asignación.** Relacionan el software con lo que no es software. Responden: ¿en qué procesador se ejecuta cada elemento? (despliegue), ¿en qué directorios o archivos se guarda durante el desarrollo, las pruebas y la construcción? (implementación), ¿qué equipo hace cada módulo? (asignación de trabajo).', 'asignacion'),
    ('callout', '**Tomado en 2024.** El parcial preguntó qué preguntas responden las estructuras de asignación y el recuperatorio, cuáles responden las de componentes y conectores. El simulacro pidió reconocer «Módulos» entre distractores como «Lógica» o «Componentes y conductores».', 'examen'),
])

S('escenarios', 'b2', 'Atributos y escenarios de calidad', 'Celina, págs. 24–29', 'PF, págs. 45–50 · Bass et al., pág. 65 (fig. 3.1)', [
    ('p', 'Un **atributo de calidad** es una propiedad medible que indica qué tan bien el sistema satisface a los interesados más allá de su funcionalidad. Ejemplos: disponibilidad, desplegabilidad, eficiencia energética, integrabilidad, modificabilidad, rendimiento, seguridad, capacidad de prueba, usabilidad.', 'que'),
    ('p', 'Decir «que sea modificable» no alcanza. Para evitar definiciones no comprobables, categorías que se solapan y vocabularios distintos, los requisitos de calidad se escriben como **escenarios de seis partes**:', 'porque'),
    ('li', '**Fuente del estímulo:** quién o qué lo genera. Importa: no se trata igual un pedido de un usuario confiable.', 'fuente'),
    ('li', '**Estímulo:** evento que llega al sistema (un pedido de cambio, un ataque, una operación).', 'estimulo'),
    ('li', '**Artefacto:** lo que recibe el estímulo: el sistema, un conjunto de sistemas o una parte.', 'artefacto'),
    ('li', '**Entorno:** circunstancias en que ocurre: operación normal, sobrecarga, o incluso en desarrollo o pruebas.', 'entorno'),
    ('li', '**Respuesta:** actividad que resulta; lo que el arquitecto debe lograr.', 'respuesta'),
    ('li', '**Medida de la respuesta:** cómo se comprueba que se cumplió. Sin medida no se puede saber si la decisión fue correcta.', 'medida'),
    ('h', 'Tácticas y patrones'),
    ('li', 'Una **táctica** es una decisión de diseño que influye en cómo responde el sistema a un estímulo; apunta a un solo atributo.', 'tactica'),
    ('li', 'Un **patrón arquitectónico** es una solución probada a un problema recurrente; suele empaquetar varias tácticas.', 'patron'),
    ('li', 'Las tácticas sirven para adaptar un patrón, para construir un diseño cuando no hay patrón y para sistematizar el análisis.', 'paraque'),
    ('callout', 'De todos los atributos, la cátedra desarrolla dos: **modificabilidad** y **rendimiento**.', 'enfasis'),
])

S('modif', 'b2', 'Modificabilidad', 'Celina, págs. 30–35', 'PF, págs. 51–60 · Bass et al., págs. 159–161', [
    ('p', 'La modificabilidad trata del **cambio**: bajar el tiempo, el costo y el riesgo de hacerlo. El simulacro la define como la capacidad de un sistema de ser cambiado o mejorado para satisfacer las necesidades de un usuario durante su vida productiva.', 'def'),
    ('li', 'Preguntas de partida: **¿qué puede cambiar?**, ¿qué probabilidad tiene?, **¿cuándo y quién** hace el cambio? (en el código, al compilar, al construir, al configurar o en ejecución) y **¿cuánto cuesta?**', 'preguntas'),
    ('li', 'Hay dos costos: el de **introducir el mecanismo** que hace modificable al sistema y el de **hacer la modificación** usándolo.', 'costos'),
    ('li', 'Variantes: **escalabilidad** (horizontal, agregar unidades; vertical, agregar recursos a una unidad; en la nube, elasticidad), **variabilidad** (producir variantes planificadas, clave en líneas de productos), **portabilidad** e **independencia de ubicación**.', 'variantes'),
    ('h', 'Tácticas'),
    ('li', '**Aumentar la cohesión:** dividir el módulo y redistribuir responsabilidades.', 'cohesion'),
    ('li', '**Reducir el acoplamiento:** encapsular, usar un intermediario, abstraer servicios comunes y restringir dependencias (como en capas, donde una capa solo usa las inferiores).', 'acoplamiento'),
    ('li', '**Aplazar la vinculación (diferir el enlace):** cuanto más tarde se fijan los valores, más barato es el cambio. En compilación: reemplazo de componentes, parametrización, aspectos. En despliegue o inicio: vinculación en tiempo de configuración, archivos de recursos. En ejecución: descubrimiento, interpretar parámetros, repositorios compartidos, polimorfismo.', 'vinculacion'),
    ('h', 'Patrones asociados'),
    ('li', 'Cliente-servidor, microkernel (plug-in), capas y publicador-suscriptor.', 'patrones'),
])

S('perf', 'b2', 'Rendimiento (performance)', 'Celina, págs. 35–38', 'PF, págs. 61–68 · Bass et al., págs. 177 y 183', [
    ('p', 'El rendimiento trata del **tiempo** y de la capacidad del sistema para cumplir requisitos temporales. El estímulo es la llegada de eventos; la medida, latencia, plazo o tasa de procesamiento.', 'def'),
    ('li', 'Dos factores componen el tiempo de respuesta: **tiempo de procesamiento** (el sistema trabaja y consume recursos) y **tiempo bloqueado** (espera por contención de recursos).', 'factores'),
    ('h', 'Tácticas'),
    ('li', '**Controlar la demanda de recursos:** gestionar las solicitudes de trabajo (llegada de eventos, frecuencia de muestreo), limitar la respuesta a eventos, priorizar eventos, reducir la sobrecarga computacional (menos intermediarios, recursos que se comunican en el mismo lugar), limitar los tiempos de ejecución y aumentar la eficiencia.', 'demanda'),
    ('li', '**Gestionar los recursos:** aumentar los recursos, introducir concurrencia, mantener múltiples copias de los cálculos (balanceo), mantener múltiples copias de los datos (replicación y caché), limitar el tamaño de las colas y programar los recursos.', 'recursos'),
    ('callout', 'Tensión con modificabilidad: un intermediario baja el acoplamiento pero agrega sobrecarga. Por eso «reducir la indirección» es una táctica de rendimiento.', 'tension'),
    ('h', 'Patrones asociados'),
    ('li', 'Service mesh, balanceador de carga (ojo: puede ser cuello de botella o punto único de falla), throttling y map-reduce.', 'patrones'),
])

S('capas', 'b2', 'Arquitectura en capas', 'Celina, págs. 43–46', 'PF, págs. 69–74 · Sommerville (2016), págs. 178–180', [
    ('p', 'Organiza el sistema en **capas de funcionalidad relacionada**. Cada capa ofrece servicios a la de arriba y **depende solo de la inmediatamente inferior**; las capas de abajo son las más centrales.', 'def'),
    ('li', 'Capas genéricas: interfaz de usuario; gestión de la interfaz, autenticación y autorización; lógica de negocio y funcionalidad de la aplicación; soporte del sistema (sistema operativo, base de datos).', 'genericas'),
    ('li', '**Cuándo:** para construir sobre sistemas existentes, cuando hay varios equipos (uno por capa) o cuando se necesita seguridad multinivel.', 'cuando'),
    ('li', '**Ventajas:** se puede **reemplazar una capa completa si se mantiene su interfaz**; es portable (solo cambian las capas atadas a la plataforma); apunta a la **modificabilidad**.', 'ventajas'),
    ('li', '**Desventajas:** en la práctica cuesta separar limpiamente las capas y a veces una capa alta habla directo con una baja; el rendimiento puede sufrir porque cada pedido atraviesa varias capas.', 'desventajas'),
    ('callout', 'Una capa es lógica, **no física**: no confundir capa (layer) con nivel (tier).', 'ojo'),
    ('li', '**MVC** separa presentación e interacción de los datos: modelo, vista y controlador. Permite cambiar los datos sin tocar su representación; puede agregar complejidad si el modelo es simple.', 'mvc'),
])

S('repocs', 'b2', 'Repositorio y cliente-servidor', 'Celina, págs. 46–48', 'PF, págs. 56–57 y 75–77 · Sommerville (2016), págs. 181 y 183', [
    ('h', 'Repositorio (pizarrón)'),
    ('li', 'Todos los datos se gestionan en un **depósito central** accesible a todos los componentes; los componentes **no interactúan entre sí**, solo a través del repositorio.', 'repo'),
    ('li', '**Cuándo:** grandes volúmenes de información que se guardan por mucho tiempo, o sistemas dirigidos por datos.', 'repocuando'),
    ('li', '**Ventajas:** componentes independientes; los datos se manejan de forma consistente y es fácil hacer backup. **Desventajas:** es un punto único de falla y distribuirlo es difícil.', 'repopros'),
    ('h', 'Cliente-servidor'),
    ('li', 'El sistema se presenta como **servicios**, cada uno ofrecido por un servidor; los **clientes** los usan. Pueden ser procesos separados en la misma máquina o en máquinas distintas.', 'cs'),
    ('li', 'La relación es **asimétrica**: el cliente conoce al servidor (lo ubica con algún mecanismo de **descubrimiento**), pero el servidor no conoce de antemano a sus clientes.', 'asimetria'),
    ('li', 'El servidor puede ser **con o sin estado**. Sin estado, cada pedido es independiente; con estado, cada pedido identifica al cliente y hace falta cerrar la sesión o un tiempo de espera.', 'estado'),
    ('li', '**Ventajas:** servidores distribuibles en la red, bajo acoplamiento, servicios compartidos. **Desventajas:** cada servidor es punto único de falla y blanco de denegación de servicio; el rendimiento depende de la red.', 'cspros'),
])

S('pipes', 'b2', 'Tuberías y filtros · Microkernel', 'Celina, págs. 48–49', 'PF, págs. 78–85 · Sommerville (2016), págs. 183–184', [
    ('h', 'Tuberías y filtros'),
    ('li', 'El procesamiento se organiza como una **cadena de transformaciones** (filtros) conectadas por tuberías: la salida de una es la entrada de la siguiente.', 'pf'),
    ('li', '**Cuándo:** procesamiento por lotes o de flujos de datos, sistemas embebidos; poca o ninguna interacción con el usuario.', 'pfcuando'),
    ('li', '**Ventajas:** fácil de entender, reutiliza transformaciones, se agregan pasos sin tocar los demás, puede ser secuencial o concurrente. **Desventaja:** hay que acordar el formato de los datos; cada filtro debe interpretar su entrada y generar su salida, lo que agrega sobrecarga.', 'pfpros'),
    ('h', 'Microkernel (plug-in)'),
    ('li', 'Un **sistema central** con la funcionalidad mínima y **plug-ins** independientes que la amplían por medio de interfaces fijas. Ejemplos: Eclipse, las extensiones de un navegador.', 'mk'),
    ('li', 'Da extensibilidad, adaptabilidad y aislamiento. Los plug-ins pueden agregarse **en ejecución** o **en compilación**.', 'mkpros'),
    ('callout', '**Tomado en 2024:** describían Eclipse (núcleo con servicios básicos y lenguajes que se instalan después) y había que reconocer Microkernel. «Sistema central y componentes extendidos» era un distractor.', 'examen'),
])

S('dist', 'b2', 'Sistemas distribuidos', 'Celina, págs. 50–53', 'PF, págs. 86–91 · Sommerville (2016), págs. 493–499', [
    ('p', 'Un sistema distribuido es «una colección de computadoras independientes que se presenta al usuario como un único sistema coherente» (Tanenbaum y Van Steen).', 'def'),
    ('li', '**Beneficios:** uso compartido de recursos, apertura (protocolos estándar), **concurrencia**, **escalabilidad** y tolerancia a fallos.', 'beneficios'),
    ('li', '**Escalabilidad** en tres dimensiones: tamaño, distribución geográfica y administrabilidad. Esta última suele ser la que limita.', 'escalabilidad'),
    ('li', '**Seguridad:** hay que protegerse de intercepción, interrupción, modificación y fabricación. Se complica cuando partes del sistema son de organizaciones distintas.', 'seguridad'),
    ('li', '**Calidad de servicio y gestión de fallos:** los fallos son inevitables; el sistema debe detectarlos, seguir dando servicio y recuperarse.', 'qos'),
    ('li', '**Desventajas:** complejidad, seguridad, manejabilidad e **imprevisibilidad** (la respuesta depende de la carga del sistema y de la red).', 'desventajas'),
    ('callout', 'En el simulacro, «predictibilidad de la red» y «consistencia estricta» eran distractores: son dificultades, no ventajas.', 'examen'),
])

S('topo', 'b2', 'Patrones para sistemas distribuidos', 'Celina, págs. 53–58', 'PF, págs. 92–105 · Sommerville (2016), págs. 500–513', [
    ('li', '**Maestro-esclavo.** El maestro se encarga del cómputo, la coordinación y las comunicaciones y controla a los esclavos, dedicados a acciones específicas (leer sensores, manejar actuadores). Para tiempo real con tiempos de respuesta garantizados.', 'me'),
    ('li', '**Cliente-servidor de dos niveles.** Un servidor lógico y muchos clientes. **Cliente liviano:** solo presentación; fácil de administrar, carga al servidor y a la red. **Cliente pesado:** procesa en el cliente; aprovecha su capacidad pero hay que instalar y mantener software en cada equipo.', 'dos'),
    ('li', '**Cliente-servidor multinivel.** Presentación, procesamiento, gestión de datos y base de datos corren como **procesos separados**. Más escalable: cada nivel se administra aparte. Para alto volumen de transacciones.', 'multi'),
    ('li', '**Componentes distribuidos.** Componentes que ofrecen servicios por su interfaz y se comunican a través de **middleware**. Abierto y flexible, pero complejo y sin estándares universales; fue desplazado por SOA.', 'comp'),
    ('li', '**Peer-to-peer (P2P).** Descentralizado: cualquier nodo calcula y no hay distinción entre cliente y servidor. Redundante y tolerante a fallos; con sobrecarga de comunicación y problemas de seguridad. Sirve para cómputo intensivo divisible o intercambio de información entre pares. La variante semicentralizada usa superpares.', 'p2p'),
])

S('soa', 'b2', 'Arquitectura orientada a servicios (SOA)', 'Celina, págs. 58–60', 'PF, págs. 106–109 · Sommerville (2016), pág. 526 (fig. 18.2)', [
    ('p', 'En SOA los componentes son **servicios independientes**, distribuidos geográficamente e independientes de la plataforma y del lenguaje. Un **servicio web** es un componente reutilizable y débilmente acoplado que encapsula una funcionalidad y se accede con protocolos estándar basados en Internet y XML.', 'def'),
    ('li', 'A diferencia de un componente, un servicio **solo tiene interfaz «provee»**: no requiere que haya otros componentes presentes.', 'provee'),
    ('li', 'Tres roles: el **proveedor** publica el servicio en el **registro**; el **solicitante** lo encuentra allí y se enlaza con el proveedor.', 'roles'),
    ('table', [['Estándar', 'Función'],
               ['SOAP', 'Intercambio de mensajes entre servicios.'],
               ['WSDL', 'Definición de la interfaz del servicio: operaciones y enlaces.'],
               ['WS-BPEL', 'Lenguaje de flujo de trabajo para procesos que involucran varios servicios.'],
               ['UDDI', 'Descubrimiento de servicios. En desuso.']], 'estandares'),
    ('li', '**Ventajas:** cualquier proveedor puede ofrecer servicios, se puede cambiar de proveedor en ejecución, se paga por uso y las aplicaciones quedan más chicas.', 'ventajas'),
])

S('micro', 'b2', 'Microservicios', 'Celina, págs. 60–61', 'Word de la cátedra (WM), págs. 136–152 · PF, págs. 110–113 · Copia de Apunte Diseño, pág. 169', [
    ('p', 'Estilo que desarrolla una aplicación como un **conjunto de servicios pequeños**, cada uno en su propio proceso y comunicado por mecanismos livianos. Son autónomos, livianos, desplegables de forma independiente y orientados al negocio.', 'def'),
    ('li', 'Resuelve dos problemas del monolito: reconstruir todo ante cada cambio y escalar con servidores más grandes. Con microservicios se replica solo el servicio exigido (**escalar horizontalmente**).', 'problema'),
    ('li', '**Contexto delimitado (bounded context):** cada servicio modela un dominio o flujo de trabajo e incluye todo lo que necesita, incluso su esquema de base de datos. Se **prefiere duplicar a acoplar**.', 'contexto'),
    ('li', '**Granularidad:** «microservicio es una etiqueta, no una descripción». El error típico es hacerlos demasiado chicos. Pautas para el límite: propósito (cohesión funcional), transacciones y cuánta comunicación exigen.', 'granularidad'),
    ('li', '**Aislamiento de datos:** cada servicio es dueño de sus datos; no hay base compartida como punto de integración. Evitar la «trampa de las entidades» (un servicio por tabla).', 'datos'),
    ('li', '**Capa de API:** punto de entrada entre consumidores y servicios; es opcional. Sirve como proxy o para servicios operativos, pero **no debe orquestar** ni tener lógica de negocio.', 'api'),
    ('li', '**Coreografía:** sin coordinador central; cada servicio llama a los que necesita. Máximo desacoplamiento, pero errores y coordinación más difíciles.', 'coreografia'),
    ('li', '**Orquestación:** un servicio mediador local coordina el flujo. Simplifica la coordinación a cambio de algo de acoplamiento.', 'orquestacion'),
    ('li', '**Saga y transacciones compensatorias:** si una parte falla, el mediador pide deshacer a las que tuvieron éxito. Se implementa con estado pendiente o con operaciones hacer/deshacer. Usar con moderación.', 'saga'),
    ('li', 'Puntos fuertes: **escalabilidad, elasticidad y capacidad evolutiva**. Es más compleja de manejar que un monolito.', 'fuertes'),
    ('callout', 'Topología para reconocer en una figura: peticiones del cliente → capa de API → servicios, cada uno con sus módulos y su propia base de datos. Salió en el simulacro 2024.', 'examen'),
])

S('saas', 'b2', 'Software como servicio (SaaS)', 'PF, pág. 114', 'Sommerville (2016), págs. 513–517', [
    ('p', 'SaaS **no es un estilo arquitectónico**: es un **modelo de entrega y de negocio**. El software se aloja de forma remota y se accede por Internet; lo controla el proveedor, no quien lo usa.', 'def'),
    ('li', 'No es lo mismo que SOA: SOA es una forma de estructurar un sistema con servicios; SaaS es una forma de ofrecerlo.', 'vs'),
    ('li', 'Ventajas: sin licencias por equipo y actualizaciones centralizadas. Desventajas: dependencia de la red y de la evolución que decida el proveedor.', 'pros'),
    ('callout', 'Prioridad C: el profesor no hizo hincapié; alcanza con distinguir modelo de entrega de estilo arquitectónico.', 'nota'),
])

# ═══════════════════════════ B3 · PUDS
S('puds', 'b3', 'PUDS: visión general', 'Celina, págs. 62–64', 'PF, págs. 115–126 · PUDS, págs. 29–34 · Copia de Apunte Diseño, pág. 206 (4P + H)', [
    ('p', 'El Proceso Unificado es un **marco de trabajo genérico** de desarrollo de software, especializable para distintos sistemas, organizaciones y tamaños de proyecto. Está **basado en componentes** conectados por interfaces y usa UML.', 'def'),
    ('li', '**Dirigido por casos de uso.** Un caso de uso es un fragmento de funcionalidad que da al usuario un resultado de valor. Los casos de uso no solo inician el proceso: son el **hilo conductor** del análisis, el diseño, la implementación y la prueba.', 'cu'),
    ('li', '**Centrado en la arquitectura.** La arquitectura es una vista del diseño completo con lo más importante, sin los detalles. Los casos de uso deben encajar en ella y, a la vez, guían su desarrollo: **evolucionan en paralelo**. Empieza como un boceto desde la fase de inicio.', 'arq'),
    ('li', '**Iterativo e incremental.** El trabajo se divide en miniproyectos: cada **iteración** produce un **incremento**. Las iteraciones se planifican y se atacan primero los riesgos mayores.', 'iter'),
    ('li', 'Ventajas de iterar: el riesgo queda acotado al costo de un incremento, baja el riesgo de no llegar al mercado a tiempo, acelera el ritmo y acepta requisitos cambiantes. En el simulacro, la razón principal es **manejar mejor los riesgos y permitir la retroalimentación temprana**.', 'ventajas'),
    ('li', 'Influyen en la arquitectura: los casos de uso más importantes, los requisitos no funcionales y los patrones arquitectónicos, entre otros.', 'influye'),
    ('li', '**Las 4 P + H:** Personas, Proyecto, Producto y Proceso, más las Herramientas que automatizan el proceso. El proceso es la plantilla del proyecto y debe estar orientado a las personas.', '4p'),
    ('callout', 'Las tres características son «innegociables»: no se puede hablar de PU sin casos de uso.', 'enfasis'),
])

S('ciclo', 'b3', 'PUDS: ciclo de vida y conceptos', 'Celina, págs. 64–65 y 73', 'PF, págs. 127–140 · PUDS, págs. 37 y 124', [
    ('p', 'El PU **se repite a lo largo de una serie de ciclos** que forman la vida del sistema. **Cada ciclo termina con una versión del producto** (release) y **consta de cuatro fases**; cada fase se divide en **iteraciones**, y cada iteración recorre los flujos de trabajo.', 'ciclo'),
    ('callout', 'Jerarquía: **ciclo → fase → iteración**. «Cada fase se divide en ciclos» y «cada ciclo se divide en iteraciones» son falsas (recuperatorio 2024).', 'jerarquia'),
    ('li', 'El **producto** no es solo el ejecutable: incluye los modelos de casos de uso, análisis, diseño, despliegue, implementación y prueba, y la descripción de la arquitectura. Todos tienen **trazas** hacia el modelo de casos de uso.', 'producto'),
    ('li', '**Flujo de trabajo fundamental (disciplina):** conjunto de actividades afines: requisitos, análisis, diseño, implementación y prueba. Su intensidad varía según la fase.', 'flujo'),
    ('li', '**Trabajador:** un rol, no una persona. Una persona puede cumplir varios roles y un rol puede asignarse a varias personas.', 'trabajador'),
    ('li', '**Actividad:** trabajo que realiza un trabajador, con artefactos de entrada y de salida.', 'actividad'),
    ('li', '**Artefacto:** cualquier cosa que se produce o usa: modelos, documentos, código. Están bajo control de versiones.', 'artefacto'),
    ('li', '**Hito:** punto de control al final de una fase (hito mayor) o de una iteración (hito menor) en el que se decide si se sigue o se ajusta.', 'hito'),
    ('li', 'PU y RUP no son lo mismo: RUP deriva del PU, agrega disciplinas y es más detallado. Lo que RUP llama rol, el PU lo llama trabajador; disciplina equivale a flujo de trabajo.', 'rup'),
])

S('fases', 'b3', 'PUDS: fases e hitos', 'Celina, págs. 65–67', 'PF, págs. 141–146 · PUDS, págs. 36–38', [
    ('table', [['Fase', 'Foco', 'Artefactos principales', 'Hito'],
               ['Inicio', 'Definir el producto y el análisis de negocio: **delimitar el alcance**, bosquejar la arquitectura, identificar riesgos críticos y **demostrar que el sistema puede resolver el problema**.', 'Lista de características, primera versión del modelo del negocio, principales requisitos como casos de uso, boceto de la arquitectura, plan preliminar.', 'Objetivos del ciclo de vida'],
               ['Elaboración', 'Detallar la mayoría de los casos de uso y **establecer la línea base de la arquitectura**. Eliminar los riesgos mayores y planificar la construcción.', 'Línea base ejecutable de la arquitectura, modelos de casos de uso y análisis, plan del proyecto para construcción y transición.', 'Arquitectura del ciclo de vida'],
               ['Construcción', 'Desarrollar el producto completo sobre la arquitectura.', 'Software ejecutable con capacidad operativa inicial, casos de prueba, manuales, arquitectura mantenida y mínimamente actualizada.', 'Capacidad operativa inicial'],
               ['Transición', 'Versión beta con usuarios reales; corregir defectos, capacitar y dar soporte.', 'Los de construcción, ya instalados donde deben funcionar.', 'Lanzamiento del producto']], 'tabla'),
    ('li', 'La arquitectura es el **esqueleto**; en elaboración se le agregan los «músculos» básicos. Al final de elaboración debe ser estable, porque cambiarla después cuesta mucho.', 'esqueleto'),
    ('li', 'El artefacto más importante de construcción es el **software ejecutable**: una versión funcional completa, aunque no libre de errores.', 'ejecutable'),
    ('li', 'Transición **no es mantenimiento**: termina el ciclo con el producto funcionando en el sitio del cliente.', 'transicion'),
    ('callout', '**Tomado en 2024.** Inicio: delimitar el alcance y demostrar que el sistema resuelve el problema (capturar el 80% de los casos de uso y la línea base son de elaboración). Construcción: el ejecutable con capacidad operativa inicial y la descripción de la arquitectura actualizada.', 'examen'),
])

S('req', 'b3', 'Requisitos y contexto del sistema', 'Celina, págs. 67–73', 'PF, págs. 147–159 · PUDS, págs. 144–145', [
    ('p', 'Capturar requisitos es averiguar **qué se debe construir**. Es difícil porque los usuarios no siempre saben qué quieren y cambiar tarde es caro.', 'que'),
    ('li', '**Enumerar los requisitos candidatos:** una **lista de características** con nombre, descripción, estado (propuesto, aprobado, incluido, validado), costo estimado, prioridad y riesgo. Se usa para **planificar** el trabajo.', 'lista'),
    ('li', '**Comprender el contexto del sistema:** con un modelo del dominio o un modelo del negocio.', 'contexto'),
    ('li', '**Modelo del dominio:** clases conceptuales del contexto (objetos del negocio, del mundo real y sucesos), en diagramas de clases. Es un caso simplificado del modelo del negocio.', 'dominio'),
    ('li', '**Modelo del negocio:** formado por el **modelo de casos de uso del negocio** y el **modelo de objetos del negocio**. Describe los procesos de la organización, no la interacción con el sistema. No siempre se hace, porque lleva tiempo.', 'negocio'),
    ('li', '**Capturar requisitos funcionales:** como **casos de uso** del sistema.', 'funcionales'),
    ('li', '**Capturar requisitos no funcionales:** los específicos van con su caso de uso; los que no pueden asociarse a uno solo son **requisitos adicionales** (de interfaz, físicos, restricciones de diseño y de implementación).', 'adicionales'),
    ('h', 'Artefactos del flujo'),
    ('li', 'Modelo de casos de uso (actores y casos de uso), descripción de la arquitectura (vista del modelo de casos de uso), **glosario** y **prototipo de interfaz de usuario**.', 'artefactos'),
    ('callout', 'Una **clase de análisis** no es un artefacto de requisitos (simulacro 2024).', 'examen'),
])

S('freq', 'b3', 'Flujo de trabajo de Requisitos', 'Celina, págs. 73–80 (figura en 75)', 'PF, págs. 160–166 y 252 · PUDS, fig. 7.10', [
    ('table', [['Trabajador', 'Actividad', 'Qué hace'],
               ['Analista de sistemas', 'Encontrar actores y casos de uso', 'Delimita el sistema, encuentra actores y casos de uso, los describe brevemente y arma el glosario.'],
               ['Arquitecto', 'Priorizar los casos de uso', 'Decide cuáles se desarrollan en las primeras iteraciones: los significativos para la arquitectura.'],
               ['Especificador de casos de uso', 'Detallar un caso de uso', 'Describe el flujo de sucesos: cómo empieza, cómo termina, precondiciones, postcondiciones y caminos alternativos.'],
               ['Diseñador de interfaz de usuario', 'Prototipar la interfaz de usuario', 'Diseño lógico y físico de la interfaz; valida que los casos de uso se entendieron.'],
               ['Analista de sistemas', 'Estructurar el modelo de casos de uso', 'Extrae lo común con generalización, inclusión y extensión.']], 'tabla'),
    ('li', 'Orden de la figura: encontrar actores y casos de uso → priorizar → detallar → prototipar; de detallar sale también estructurar el modelo.', 'orden'),
    ('li', 'El **analista de sistemas** es responsable del conjunto del modelo: define el límite del sistema, los actores y los casos de uso, pero no detalla cada uno.', 'analista'),
    ('li', 'El **arquitecto** aparece en todos los flujos salvo en prueba.', 'arquitecto'),
    ('callout', '**Tomado en el parcial 2024:** completar la figura con Analista de sistemas, Arquitecto, Diseñador de interfaz de usuario, y las actividades Encontrar actores y casos de uso, Priorizar, Detallar y Prototipar.', 'examen'),
])

S('crc', 'b3', 'Realización de casos de uso y tarjetas CRC (práctica)', 'PF, págs. 167–175', 'Apunte de Fidanza, pág. 19 (CRC)', [
    ('p', 'Una realización de caso de uso muestra cómo colaboran las clases para llevar a cabo el caso de uso. Tiene una **parte estática** (diagrama de clases) y una **dinámica** (diagrama de secuencia).', 'que'),
    ('li', 'Se parte de las **responsabilidades** (conocer y hacer), se asignan a clases con tarjetas **CRC** (Clase, Responsabilidad, Colaboración) y se dibuja la interacción.', 'crc'),
    ('h', 'Acuerdos de la cátedra'),
    ('li', 'Poner **solo las clases necesarias** para ese caso de uso.', 'solo'),
    ('li', 'Por cada realización hay **un controlador y una interfaz**, con el nombre del caso de uso. La clase interfaz colabora solo con el controlador.', 'ctrl'),
    ('li', 'Se dibuja siempre el **camino feliz**, no los alternativos.', 'feliz'),
    ('li', 'Los actores secundarios van a la derecha, al final.', 'secundarios'),
    ('callout', 'Prioridad B y de práctica: no aparece en los registros de teoría de 2024.', 'nota'),
])

S('man', 'b3', 'Modelo de análisis', 'Celina, págs. 81–87', 'PF, págs. 176–185 · PUDS, págs. 187–208', [
    ('p', 'En análisis se refinan y estructuran los requisitos **en el lenguaje de los desarrolladores**, para entenderlos mejor y dar una primera forma al sistema.', 'que'),
    ('table', [['Modelo de casos de uso', 'Modelo de análisis'],
               ['Descrito con el lenguaje del cliente.', 'Descrito con el lenguaje del desarrollador.'],
               ['Vista externa del sistema.', 'Vista interna del sistema.'],
               ['Estructurado por los casos de uso.', 'Estructurado por clases y paquetes estereotipados.'],
               ['Contrato entre el cliente y los desarrolladores.', 'Lo usan los desarrolladores para comprender cómo dar forma al sistema.'],
               ['Puede contener redundancias e inconsistencias entre requisitos.', 'No debería contenerlas.'],
               ['Captura la funcionalidad.', 'Esboza cómo llevarla a cabo: primera aproximación al diseño.'],
               ['Define casos de uso.', 'Define realizaciones de casos de uso.']], 'vs'),
    ('h', 'Artefactos'),
    ('li', '**Clase del análisis:** se centra en requisitos funcionales, su comportamiento se define por **responsabilidades** a alto nivel y **siempre** encaja en uno de tres estereotipos.', 'clase'),
    ('li', '**Interfaz (frontera):** interacción entre el sistema y sus actores. **Entidad:** información duradera. **Control:** coordinación, secuencia y lógica que no encaja en las otras.', 'estereotipos'),
    ('li', '**Realización de caso de uso-análisis:** una **colaboración** dentro del modelo de análisis, con **traza directa** al caso de uso. Tiene diagramas de clases, diagramas de interacción (se prefieren los de **colaboración**), flujo de sucesos-análisis y requisitos especiales.', 'realizacion'),
    ('li', '**Paquete del análisis:** organiza el modelo en piezas manejables; probablemente se convierta en subsistema en diseño. El **paquete de servicio** agrupa clases que dan un servicio indivisible.', 'paquete'),
    ('li', '**Descripción de la arquitectura (vista del modelo de análisis):** paquetes, clases clave y realizaciones significativas.', 'arq'),
    ('callout', 'En análisis no hay subsistemas ni navegabilidad, y los atributos no usan tipos del lenguaje de programación.', 'ojo'),
])

S('fan', 'b3', 'Flujo de trabajo de Análisis', 'Celina, págs. 87–92 (figura en 88)', 'PF, págs. 186–191 y 256 · PUDS, fig. 8.18', [
    ('table', [['Trabajador', 'Actividad', 'Qué hace'],
               ['Arquitecto', 'Análisis de la arquitectura', 'Identifica paquetes del análisis, clases de entidad obvias y requisitos especiales comunes.'],
               ['Ingeniero de casos de uso', 'Analizar un caso de uso', 'Identifica las clases del análisis, describe las interacciones entre objetos y captura requisitos especiales.'],
               ['Ingeniero de componentes', 'Analizar una clase', 'Identifica responsabilidades, atributos, asociaciones, agregaciones y generalizaciones.'],
               ['Ingeniero de componentes', 'Analizar un paquete', 'Cuida que el paquete sea independiente y cumpla su objetivo; describe sus dependencias.']], 'tabla'),
    ('li', 'El **analista de sistemas no participa** en este flujo: su trabajo está en requisitos.', 'analista'),
    ('li', 'El **ingeniero de casos de uso** responde por la integridad de las realizaciones, tanto en análisis como en diseño.', 'ingcu'),
    ('callout', 'En el simulacro 2024 había que emparejar trabajador y actividad: «Realizar caso de uso» no existe; la actividad es analizar un caso de uso.', 'examen'),
])

S('mdis', 'b3', 'Modelo de diseño', 'Celina, págs. 93–99', 'PF, págs. 192–203 · PUDS, págs. 227–242', [
    ('p', 'En diseño se da forma al sistema para que soporte todos los requisitos, incluidos los no funcionales y las restricciones. El modelo de diseño es un **plano de la implementación**.', 'que'),
    ('table', [['Modelo de análisis', 'Modelo de diseño'],
               ['Conceptual: una abstracción del sistema.', 'Físico: un plano de la implementación.'],
               ['Genérico respecto del diseño.', 'Específico para una implementación.'],
               ['Tres estereotipos: control, entidad e interfaz.', 'Cualquier número de estereotipos, según el lenguaje.'],
               ['Menos formal.', 'Más formal.'],
               ['Dinámico, pero no muy centrado en la secuencia.', 'Dinámico y muy centrado en la secuencia.'],
               ['Puede no mantenerse durante todo el ciclo de vida.', 'Debe mantenerse durante todo el ciclo de vida.'],
               ['Bosquejo del diseño.', 'Manifiesto del diseño.']], 'vs'),
    ('h', 'Artefactos'),
    ('li', '**Clase del diseño:** se especifica con el lenguaje de programación; los **atributos se declaran con sus tipos**, se define la visibilidad y sus relaciones tienen un significado directo al implementar. Los métodos pueden quedar en lenguaje natural o pseudocódigo.', 'clase'),
    ('li', '**Realización de caso de uso-diseño:** colaboración en el modelo de diseño, con traza a la realización de análisis (o **directa al caso de uso** si no hay análisis). Tiene diagramas de clases, diagramas de interacción (se prefieren los de **secuencia**, que pueden incluir subsistemas), flujo de sucesos-diseño y requisitos de implementación.', 'realizacion'),
    ('li', '**Subsistema de diseño:** organiza el modelo en piezas; debe ser cohesivo y débilmente acoplado. El **subsistema de servicio** viene de un paquete de servicio.', 'subsistema'),
    ('li', '**Interfaz:** operaciones que ofrecen las clases y los subsistemas.', 'interfaz'),
    ('li', '**Modelo de despliegue:** nodos y sus conexiones; distribuye la funcionalidad entre los nodos.', 'despliegue'),
    ('callout', '**Tomado en 2024:** una clase de diseño puede participar en varias realizaciones; el flujo de sucesos-diseño sí habla de objetos o subsistemas que interactúan.', 'examen'),
])

S('fdis', 'b3', 'Flujo de trabajo de Diseño', 'Celina, págs. 99–107 (figura en 100)', 'PF, págs. 204–213 y 261 · PUDS, fig. 9.16', [
    ('table', [['Trabajador', 'Actividad', 'Qué hace'],
               ['Arquitecto', 'Diseño de la arquitectura', 'Identifica nodos y configuraciones de red, subsistemas e interfaces, clases significativas (incluidas las activas) y mecanismos genéricos como la persistencia.'],
               ['Ingeniero de casos de uso', 'Diseñar un caso de uso', 'Identifica las clases del diseño participantes a partir de las del análisis, describe las interacciones y captura requisitos de implementación.'],
               ['Ingeniero de componentes', 'Diseñar una clase', 'Esboza la clase e identifica operaciones, atributos, asociaciones y generalizaciones; describe métodos y estados.'],
               ['Ingeniero de componentes', 'Diseñar un subsistema', 'Mantiene las dependencias, las interfaces y el contenido del subsistema.']], 'tabla'),
    ('li', 'Flechas de la figura: del diseño de la arquitectura salen diseñar un caso de uso y diseñar una clase; de diseñar una clase se vuelve a diseñar un caso de uso; ambos llegan a diseñar un subsistema.', 'flechas'),
    ('li', 'A veces conviene diseñar el caso de uso **en términos de subsistemas y sus interfaces** en lugar de clases.', 'subs'),
    ('li', 'Al diseñar un subsistema, las dependencias se orientan a **interfaces**, no a clases internas de otro subsistema.', 'deps'),
    ('callout', '**Tomado en el recuperatorio 2024:** completar la figura con Ingeniero de casos de uso, Ingeniero de componentes, Diseño arquitectónico, Diseñar una clase y Diseñar un subsistema.', 'examen'),
])

S('impl', 'b3', 'Implementación', 'Celina, págs. 107–118 (figura en 113)', 'PF, págs. 214–229 y 266 · PUDS, págs. 288–292', [
    ('p', 'Se implementa el sistema en términos de **componentes**: código fuente, scripts, binarios, ejecutables. Propósitos: planificar las integraciones, **distribuir el sistema asignando componentes ejecutables a nodos**, implementar clases y subsistemas, y **probar los componentes como unidades e integrarlos** en uno o más ejecutables.', 'que'),
    ('h', 'Artefactos'),
    ('li', '**Modelo de implementación**, **componente** (empaquetamiento físico de elementos del diseño; un componente puede implementar varias clases), **subsistema de implementación**, **interfaz** y descripción de la arquitectura.', 'artefactos'),
    ('li', '**Stub:** componente con una implementación esquelética que reemplaza temporalmente a otro para poder compilar y probar.', 'stub'),
    ('li', '**Plan de integración de construcciones:** secuencia de construcciones (builds) de una iteración; para cada una, qué funcionalidad y qué partes del modelo se implementan.', 'plan'),
    ('table', [['Trabajador', 'Actividad'],
               ['Arquitecto', 'Implementación de la arquitectura'],
               ['Integrador de sistemas', 'Integrar el sistema: planificar e integrar cada construcción'],
               ['Ingeniero de componentes', 'Implementar un subsistema'],
               ['Ingeniero de componentes', 'Implementar una clase'],
               ['Ingeniero de componentes', 'Realizar prueba de unidad']], 'tabla'),
    ('li', '**Prueba de unidad:** de especificación (caja negra, comportamiento observable) y de estructura (caja blanca). Se hace **en implementación**, no en el flujo de prueba.', 'unidad'),
    ('li', 'El **ingeniero de componentes** define y mantiene el código fuente de uno o varios componentes y asegura que implementen la funcionalidad correcta.', 'ingcomp'),
])

S('prueba', 'b3', 'Prueba', 'Celina, págs. 118–127 (figura en 123)', 'PF, págs. 230–247 y 270 · PUDS, págs. 304 y 308–312', [
    ('p', 'Se verifica el resultado de la implementación probando cada construcción. Propósitos: **planificar** las pruebas de cada iteración, **diseñarlas e implementarlas**, y **realizarlas** manejando los resultados de forma sistemática.', 'que'),
    ('h', 'Artefactos'),
    ('li', '**Modelo de pruebas:** describe cómo se prueban los componentes ejecutables con pruebas de integración y de sistema.', 'modelo'),
    ('li', '**Caso de prueba:** entrada, resultado esperado y condiciones. Los de **caja negra** se derivan de los casos de uso; los de **caja blanca**, de las realizaciones de caso de uso-diseño.', 'caso'),
    ('li', '**Procedimiento de prueba:** cómo ejecutar uno o varios casos de prueba.', 'procedimiento'),
    ('li', '**Componente de prueba:** automatiza uno o varios procedimientos de prueba o partes de ellos.', 'componente'),
    ('li', '**Plan de prueba**, **defecto** (anomalía del sistema) y **evaluación de prueba** (cobertura, estado de los defectos).', 'otros'),
    ('table', [['Trabajador', 'Actividad'],
               ['Ingeniero de pruebas', 'Planificar prueba'],
               ['Ingeniero de pruebas', 'Diseñar prueba'],
               ['Ingeniero de componentes', 'Implementar pruebas'],
               ['Ingeniero de pruebas de integración', 'Realizar pruebas de integración'],
               ['Ingeniero de pruebas de sistema', 'Realizar prueba de sistema'],
               ['Ingeniero de pruebas', 'Evaluar prueba']], 'tabla'),
    ('li', 'El **arquitecto no participa** en este flujo. El ingeniero de componentes implementa los componentes de prueba.', 'quien'),
    ('li', '**Planificar** fija la estrategia, los recursos y el calendario; **diseñar** identifica casos y procedimientos de prueba de integración, de sistema y de regresión.', 'plandis'),
    ('callout', '**Clave en duda.** El simulacro 2024 daba por correcta «los casos de prueba de caja blanca se derivan de los casos de uso». El cuestionario 2026 y el libro dicen caja negra. Estudiá la versión del libro.', 'duda'),
])

S('repaso', 'b3', 'Repaso: trabajadores a lo largo de los cinco flujos', 'Celina, págs. 75, 88, 100, 113 y 123', 'PF, págs. 249–285', [
    ('table', [['Trabajador', 'Requisitos', 'Análisis', 'Diseño', 'Implementación', 'Prueba'],
               ['Analista de sistemas', 'Encontrar actores y CU; estructurar el modelo', '—', '—', '—', '—'],
               ['Especificador de casos de uso', 'Detallar un CU', '—', '—', '—', '—'],
               ['Diseñador de interfaz de usuario', 'Prototipar la interfaz', '—', '—', '—', '—'],
               ['Arquitecto', 'Priorizar los CU', 'Análisis de la arquitectura', 'Diseño de la arquitectura', 'Implementación de la arquitectura', '—'],
               ['Ingeniero de casos de uso', '—', 'Analizar un CU', 'Diseñar un CU', '—', '—'],
               ['Ingeniero de componentes', '—', 'Analizar una clase y un paquete', 'Diseñar una clase y un subsistema', 'Implementar subsistema y clase; prueba de unidad', 'Implementar pruebas'],
               ['Integrador de sistemas', '—', '—', '—', 'Integrar el sistema', '—'],
               ['Ingenieros de pruebas', '—', '—', '—', '—', 'Planificar, diseñar, realizar y evaluar']], 'tabla'),
    ('li', '**Ingeniero de casos de uso:** responsable de la integridad de las realizaciones, de que sus descripciones y diagramas sean legibles y adecuados, y tanto del análisis como del diseño del caso de uso.', 'ingcu'),
    ('li', '**Ingeniero de componentes:** define y mantiene operaciones, métodos, atributos, relaciones y requisitos de implementación de las clases de diseño, y el código fuente de los componentes.', 'ingcomp'),
    ('callout', 'Completar trabajadores y actividades fue el formato que se repitió en los dos registros reales de 2024 (Requisitos en el parcial, Diseño en el recuperatorio). Practicá los cinco en Gráficos.', 'examen'),
])

# ═══════════════════════════ B4 · Patrones GoF
S('gof', 'b4', 'Patrones de diseño: definición, formato y clasificación', 'Celina, págs. 127–132', 'PF, págs. 286–295 · GoF, págs. 12–19', [
    ('p', 'Según el GoF, los patrones de diseño son **descripciones de clases y objetos que se comunican, adaptados para resolver un problema de diseño general en un contexto particular**. No son plantillas de código ni diseños de aplicaciones completas.', 'def'),
    ('li', 'Un patrón tiene cuatro elementos esenciales: **nombre**, **problema**, **solución** y **consecuencias**.', 'elementos'),
    ('li', '**Formato GoF:** nombre y clasificación, intención, también conocido como, motivación, aplicabilidad, estructura, participantes, colaboraciones, consecuencias, implementación, código de ejemplo, usos conocidos y patrones relacionados.', 'formato'),
    ('li', '«Contexto», «fuerzas» y «racionalidad» son de la **forma de Alexander**, no del formato GoF. «Pautas» no es de ninguno.', 'alexander'),
    ('li', '**Propósito:** qué hace el patrón. **De creación** (instanciación), **estructural** (composición de clases y objetos) o **de comportamiento** (interacción y reparto de responsabilidades).', 'proposito'),
    ('li', '**Alcance:** a qué se aplica. **De clase** (relaciones por herencia, fijas en compilación) o **de objeto** (relaciones entre objetos, cambiables en ejecución).', 'alcance'),
    ('table', [['', 'De creación', 'Estructural', 'De comportamiento'],
               ['Clase', 'Factory Method', 'Adapter (de clases)', 'Interpreter, Template Method'],
               ['Objeto', 'Abstract Factory, Builder, Prototype, Singleton', 'Adapter (de objetos), Bridge, Composite, Decorator, Facade, Flyweight, Proxy', 'Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Visitor']], 'catalogo'),
    ('callout', '**Ojo con Flyweight.** La tabla de la pág. 132 de Celina lo deja en la columna de comportamiento, y la copia digital del GoF tiene el mismo corrimiento. Es **estructural de objeto**: el índice del libro lo ubica entre los estructurales.', 'flyweight'),
    ('callout', '**Lo más tomado del bloque:** la clasificación salió en el parcial, el recuperatorio y el simulacro de 2024. Adapter es el único que figura con alcance de clase y de objeto.', 'examen'),
])

S('creac', 'b4', 'Factory Method, Singleton y Abstract Factory', 'Celina, págs. 133–136', 'PF, págs. 296–299 y 305–307 · GoF, págs. 124–126, 210–212 y 307–308', [
    ('h', 'Factory Method'),
    ('li', '**Intención:** definir una interfaz para crear un objeto, pero dejar que **las subclases decidan qué clase instanciar**.', 'fm'),
    ('li', '**Participantes:** Product, ConcreteProduct, Creator (declara el método de fabricación) y ConcreteCreator (lo redefine).', 'fmpart'),
    ('li', '**Aplicabilidad:** una clase no puede prever qué objetos debe crear o quiere que lo especifiquen sus subclases. Aplica el principio abierto/cerrado.', 'fmaplic'),
    ('h', 'Singleton'),
    ('li', '**Intención:** garantizar que una clase tenga **una única instancia** y dar un **punto de acceso global** a ella. Se logra con un constructor privado y una operación de clase que devuelve la instancia.', 'sing'),
    ('h', 'Abstract Factory'),
    ('li', '**Intención:** dar una interfaz para crear **familias de objetos relacionados** sin especificar sus clases concretas.', 'af'),
    ('li', '**Participantes:** AbstractFactory, ConcreteFactory, AbstractProduct, ConcreteProduct y Client.', 'afpart'),
    ('li', 'Agregar una **familia nueva** es fácil: una fábrica concreta más. Agregar un **tipo de producto nuevo** obliga a cambiar la interfaz de la fábrica y todas las concretas.', 'afcons'),
    ('callout', '**Factory Method vs. Abstract Factory.** El primero crea un producto y usa herencia; el segundo crea familias y usa composición. Las fábricas concretas suelen implementarse con Factory Method.', 'vs'),
])

S('estruc', 'b4', 'Adapter, Composite, Facade y Proxy', 'Celina, págs. 136–141', 'PF, págs. 300–301 y 310–312 · GoF, págs. 133–135, 182–184, 203 y 298–299', [
    ('h', 'Adapter'),
    ('li', '**Intención:** convertir la interfaz de una clase en otra que los clientes esperan; permite que trabajen juntas clases con **interfaces incompatibles**.', 'adapter'),
    ('li', '**Participantes:** Target (interfaz esperada), Client, Adaptee (interfaz existente) y Adapter. De clases: hereda de ambos. De objetos: contiene al adaptado.', 'adpart'),
    ('h', 'Composite'),
    ('li', '**Intención:** componer objetos en **estructuras de árbol** para representar jerarquías parte-todo; el cliente trata **igual** a los objetos individuales y a los compuestos.', 'composite'),
    ('li', '**Participantes:** Component, Leaf (hoja), Composite (guarda hijos y delega en ellos) y Client. Declarar la gestión de hijos en Component da uniformidad, pero obliga a resolver qué hacen las hojas.', 'copart'),
    ('h', 'Facade'),
    ('li', '**Intención:** dar una **interfaz unificada** a un conjunto de interfaces de un subsistema; una interfaz de alto nivel que lo hace más fácil de usar.', 'facade'),
    ('li', '**Aplicabilidad:** interfaz simple para un subsistema complejo, reducir dependencias entre clientes y clases de implementación, y **dividir en capas** los subsistemas. No impide el acceso directo.', 'faaplic'),
    ('h', 'Proxy'),
    ('li', '**Intención:** dar un **representante o sustituto** de otro objeto para controlar el acceso a él. Participantes: Subject, RealSubject y Proxy.', 'proxy'),
    ('li', 'Tipos: **remoto** (representa un objeto de otro espacio de direcciones), **virtual** (crea objetos costosos solo cuando hacen falta) y **de protección** (verifica permisos).', 'pxtipos'),
    ('callout', '**Adapter vs. Facade.** Los dos ponen un intermediario; cambia la intención: compatibilizar una interfaz existente o simplificar el acceso a un subsistema.', 'vs'),
])

S('comport', 'b4', 'Observer, Strategy, State e Iterator', 'Celina, págs. 142–145', 'PF, págs. 302–303 y 308–309 · Copia de Apunte Diseño, págs. 197–199 (Strategy) · GoF, págs. 246, 278–280, 315 y 323–325', [
    ('h', 'Observer'),
    ('li', '**Intención:** definir una dependencia **de uno a muchos**: cuando un objeto cambia de estado, todos sus dependientes son notificados y se actualizan. Es la base de MVC.', 'observer'),
    ('li', '**Participantes:** Subject (adscribir, quitar, notificar), Observer (actualizar), ConcreteSubject y ConcreteObserver.', 'obpart'),
    ('li', '**Aplicabilidad:** un cambio en un objeto exige cambiar otros y no se sabe cuántos; un objeto debe notificar a otros sin suponer quiénes son.', 'obaplic'),
    ('h', 'Strategy'),
    ('li', '**Intención:** definir una **familia de algoritmos**, encapsular cada uno y hacerlos **intercambiables**. Participantes: Context, Strategy y ConcreteStrategy.', 'strategy'),
    ('h', 'State'),
    ('li', '**Intención:** permitir que un objeto **cambie su comportamiento cuando cambia su estado interno**; parece cambiar de clase. Participantes: Context, State y ConcreteState.', 'state'),
    ('li', 'Cada estado va en su propia clase: se evita lógica condicional repartida en muchos métodos y agregar un estado no toca el código existente.', 'stcons'),
    ('callout', '**Strategy vs. State.** La estructura es casi la misma. En Strategy el algoritmo lo elige algo externo y no implica cambio de estado; en State el cambio depende del estado interno y los propios estados pueden decidir las transiciones.', 'vs'),
    ('h', 'Iterator'),
    ('li', '**Intención:** acceder secuencialmente a los elementos de un agregado **sin exponer su representación interna**. Participantes: Iterator, ConcreteIterator, Aggregate y ConcreteAggregate.', 'iterator'),
])

# ═══════════════════════════ B5 · Agilidad y XP
S('agil', 'b5', 'Agilidad y Manifiesto Ágil', 'Celina, págs. 145–149', 'PF, págs. 313–328', [
    ('p', 'Las metodologías clásicas surgieron contra el «codificar y corregir», pero trajeron **burocracia**, **rigidez** y la ilusión de requisitos predecibles. Los métodos ágiles buscan un punto medio entre no tener proceso y tener demasiado.', 'origen'),
    ('li', 'Diferencias: son **menos orientados a la documentación** y más al código; **adaptativos en vez de predictivos**; y **orientados a las personas** más que a los procesos.', 'difs'),
    ('h', 'Valores del Manifiesto (febrero de 2001)'),
    ('li', '**Individuos e interacciones** por sobre procesos y herramientas.', 'v1'),
    ('li', '**Software funcionando** por sobre extensa documentación.', 'v2'),
    ('li', '**Colaboración del cliente** por sobre negociación contractual.', 'v3'),
    ('li', '**Responder al cambio** por sobre seguir un plan.', 'v4'),
    ('h', 'Principios que conviene reconocer'),
    ('li', 'Satisfacer al cliente con entrega temprana y continua; aceptar cambios aun tarde; **entregar software funcionando con frecuencia, de un par de semanas a un par de meses**; **negocio y desarrolladores trabajan juntos a diario**; conversación cara a cara; el software funcionando es la primera medida de progreso; ritmo sostenible; excelencia técnica; simplicidad; equipos autoorganizados; reflexión periódica.', 'principios'),
    ('h', 'Frameworks'),
    ('li', 'DSDM (1994; MoSCoW y timeboxes), Scrum (1995), XP (1996), FDD (1997), Crystal (1998) y ASD (1999; especular, colaborar, aprender). Todos comparten adaptación, colaboración y entrega frecuente.', 'frameworks'),
])

S('xp', 'b5', 'Extreme Programming (XP)', 'Celina, págs. 149–157 (gráfico en 153)', 'PF, págs. 329–342 · Beck, págs. 24–30', [
    ('p', 'XP es una metodología **liviana**, pensada para dominios con requisitos muy cambiantes y **equipos chicos (2 a 10 personas)**. Se centra en el código y da prioridad a las pruebas, que deben automatizarse.', 'que'),
    ('li', '**Valores:** simplicidad, comunicación, retroalimentación, coraje y respeto.', 'valores'),
    ('li', '**Principios centrales:** retroalimentación rápida, suponer simplicidad, cambio incremental, abrazar el cambio y trabajo de calidad.', 'principios'),
    ('li', '**Actividades básicas:** **programar, probar, escuchar y diseñar**. Analizar y planificar no figuran.', 'actividades'),
    ('li', '**Prácticas (12):** juego de la planificación, entregas pequeñas, metáfora, diseño simple, pruebas, refactorización, programación de a pares, propiedad colectiva, integración continua, semana de 40 horas, cliente en el sitio y estándares de codificación.', 'practicas'),
    ('callout', 'El profesor pidió enfocarse en **metáfora, diseño simple, refactorización y estándares de codificación**, y en saber qué es un spike.', 'enfasis'),
    ('li', '**Metáfora:** historia compartida de cómo funciona el sistema, sin términos técnicos. Reemplaza al concepto de arquitectura. Es la práctica menos usada.', 'metafora'),
    ('li', '**Diseño simple:** el diseño correcto **ejecuta todas las pruebas**, **no tiene lógica duplicada**, **declara las intenciones importantes** de los programadores y tiene **la menor cantidad de clases y métodos**. Se diseña para hoy.', 'simple'),
    ('li', '**Refactorización:** mejorar la estructura interna del código **sin alterar su comportamiento**: quitar duplicación, mejorar la legibilidad, simplificar.', 'refactor'),
    ('li', '**TDD:** práctica clave; se escriben las pruebas antes que el código.', 'tdd'),
    ('h', 'Cómo funciona el proyecto'),
    ('li', '**Historias de usuario** (las escribe el cliente) → **planificación de entregas** → **iteración** (1 a 3 semanas) → **pruebas de aceptación** (caja negra, las verifica el cliente) → aprobación del cliente → **entregas pequeñas**.', 'proyecto'),
    ('li', '**Spike:** solución muy simple para explorar una duda técnica o de diseño. Reduce el riesgo o vuelve confiable una estimación. El **spike arquitectónico** alimenta la metáfora y la planificación.', 'spike'),
    ('li', '**Limitaciones:** sin diseño formal (riesgoso en sistemas grandes), difícil con muchos usuarios, documentación limitada al código, exige gente muy capaz, sin plan de calidad.', 'limites'),
])

S('am', 'b5', 'Agile Modeling y post-agilismo', 'PF, págs. 343–344', '', [
    ('li', '**Agile Modeling:** aplicar los valores ágiles al modelado: modelar lo justo para entender y comunicar, sin documentación que nadie va a mantener.', 'am'),
    ('li', '**Post-agilismo:** tras el Manifiesto surgieron muchas propuestas «ágiles», más diluidas; después se volvió a las raíces.', 'post'),
    ('callout', 'Prioridad C: en las diapositivas son dos láminas con poco texto. Alcanza con reconocer el objetivo.', 'nota'),
])

# ═══════════════════════════ B6 · Calidad (condicional)
S('calidad', 'b6', 'Calidad del software y costo de la calidad', 'Copia de Apunte Diseño, págs. 235–238', 'PF, págs. 345–355 · Pressman, págs. 343–357', [
    ('callout', '**Bloque condicional.** Se dio en la clase del 12/11, pero el cuadro lo deja sujeto al aviso del aula. Confirmá si entra antes de dedicarle tiempo.', 'cond'),
    ('p', 'Calidad es un concepto con varias caras. Garvin distingue cinco puntos de vista: **trascendental** (se reconoce pero cuesta definirla), **del usuario** (cumple mis necesidades), **del fabricante** (cumple las especificaciones), **del producto** (características inherentes) y **basado en el valor** (lo que estoy dispuesto a pagar).', 'vistas'),
    ('li', '**Calidad de diseño:** grado en que el diseño cumple los requisitos. **Calidad de conformidad:** grado en que la implementación sigue al diseño.', 'disconf'),
    ('li', 'Pressman: un **proceso eficaz** que crea un **producto útil** que da **valor medible** a quienes lo producen y a quienes lo usan. La calidad está presente todo el tiempo, no en un momento.', 'pressman'),
    ('li', '**Modelos de factores:** McCall (operación, revisión y transición del producto) e ISO 25010 (calidad del producto). Conviene poder nombrar tres o cuatro atributos como ejemplo.', 'modelos'),
    ('li', '**Dilema de la calidad:** equilibrar calidad, tiempo y costo; lanzar software «suficientemente bueno» tiene riesgos, sobre todo para empresas chicas.', 'dilema'),
    ('h', 'Costo de la calidad'),
    ('li', '**Prevención:** planificación, capacitación, actividades técnicas. **Evaluación:** revisiones, pruebas, recolección de datos. **Fallas:** internas (antes de entregar) y externas (después; las más caras).', 'costos'),
    ('li', 'Decisiones de gestión que la afectan: estimaciones poco realistas, atajos en la planificación o las pruebas, y falta de gestión de riesgos.', 'gestion'),
    ('li', 'Cuatro pilares: métodos de ingeniería de software, buenas prácticas de gestión, **control de calidad** y **aseguramiento de la calidad**.', 'pilares'),
])

S('sqa', 'b6', 'Revisiones y aseguramiento de la calidad (SQA)', 'Copia de Apunte Diseño, págs. 237–240', 'PF, págs. 355–364 · Pressman, págs. 358–388', [
    ('p', 'Las revisiones son el **filtro de calidad** del proceso: una forma estática de control que no necesita código ejecutable. Su mayor impacto está en el diseño, donde se introduce la mayoría de los errores.', 'que'),
    ('li', '**Error:** problema encontrado antes de entregar. **Defecto:** encontrado después. Los errores se amplifican al avanzar.', 'errdef'),
    ('li', 'Esfuerzo de revisión = preparación + evaluación + retrabajo. Las revisiones no retrasan: ahorran retrabajo.', 'esfuerzo'),
    ('li', '**Informales:** poca preparación, como la revisión de escritorio o la programación de a pares. **Formales (RTF):** preparadas, con roles y registro. A mayor criticidad, más formalidad.', 'tipos'),
    ('li', 'Buenas prácticas: revisar el producto y no a la persona, seguir la agenda, marcar los problemas sin resolverlos ahí, usar listas de verificación, capacitar a los revisores y registrar los resultados.', 'practicas'),
    ('li', 'En entornos ágiles, las revisiones ocurren en la planificación del sprint, la reunión diaria, la programación de a pares, la revisión del sprint y la retrospectiva.', 'agil'),
    ('h', 'SQA'),
    ('li', '**Control de calidad (QC):** verifica el **producto** (por ejemplo, con pruebas). **Aseguramiento (QA):** se ocupa de los **procesos** con los que se hace el producto. SQA es una actividad «sombrilla» que cubre todo el proceso.', 'qaqc'),
    ('li', 'Elementos: estándares, revisiones y auditorías, pruebas, análisis de errores, gestión del cambio (da trazabilidad), formación, gestión de proveedores, seguridad y gestión de riesgos.', 'elementos'),
    ('li', 'Metas: calidad de los requisitos, del diseño y del código, y eficacia del control de calidad.', 'metas'),
])

# ═══════════════════════════ B7 · Sin confirmar
S('pend', 'b7', 'Temas de modelos viejos sin confirmar', 'Copia de Apunte Diseño, págs. 11–39', 'Apunte de Fidanza, págs. 199–222', [
    ('callout', 'Estos temas aparecen en el parcial, el recuperatorio y el simulacro de 2024, pero **no figuran en las diapositivas de 2026**. Hasta que la cátedra confirme, este repaso solo incluye las preguntas originales, en un bloque aparte.', 'aviso'),
    ('li', '**Interfaz, entradas y salidas, GUI y UX:** manipulación directa, sesgos en el diseño de salidas, ventanas modales, estilos de interacción, reglas de oro, accesibilidad, norma ISO 9241-210 y facetas de la experiencia de usuario. En 2024 fueron 3 preguntas del parcial y 2 del recuperatorio.', 'interfaz'),
    ('li', '**Diseño estructurado y Warnier:** diagrama de estructura, cohesión y acoplamiento, fan-in y fan-out, alcance de control y de efecto, diagrama de Warnier. En 2024 fue 1 pregunta del parcial y 2 del recuperatorio.', 'estructurado'),
    ('li', 'Dónde leerlos si entran: Copia de Apunte Diseño, págs. 11–39 (ventana modal en la 28, ISO 9241 en la 37, Warnier en la 10); Apunte de Fidanza, págs. 199–215 (interfaz) y 216–222 (diseño estructurado).', 'donde'),
])
