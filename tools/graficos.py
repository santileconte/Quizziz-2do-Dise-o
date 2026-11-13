"""Genera todos los gráficos de src/graficos/. Uso: python3 tools/graficos.py"""
import math
from graficos_lib import Diagram, top, bottom, left, right, at, SOFT, HEAD, BG, MUTED, LINE, ACCENT

B1 = 'B1 · Diseño orientado a objetos'
B2 = 'B2 · Arquitectura y sistemas distribuidos'
B3 = 'B3 · PUDS'
B4 = 'B4 · Patrones GoF'
B5 = 'B5 · Agilidad y XP'
B6 = 'B6 · Calidad y SQA (condicional)'
total = 0


def done(d):
    global total
    n = d.save()
    total += n
    print(f'{d.file:44} {n:3} huecos')


# ───────────────────────── B3 · PUDS: los cinco flujos de trabajo
def flujo(file, title, order, lanes, acts, arrows, fuente, w=1000):
    """Carriles por trabajador, como las figuras del PUDS.

    lanes: [(trabajador, otras respuestas, alto)]
    acts: {clave: (carril, x, texto, otras respuestas, opciones)}; opciones: lab='below' pone el rótulo debajo, dy lo baja.
    arrows: [(de, lado, a, lado, corrimiento_de, corrimiento_a)] con lados r, l, t, b; se trazan en ángulo recto.
    """
    tops, y = [], 0
    for _, _, lh in lanes:
        tops.append(y)
        y += lh
    d = Diagram(file, title, B3, order, w, y + 34, fuente)
    for i, (name, acc, lh) in enumerate(lanes):
        if i:
            d.line((14, tops[i]), (w - 14, tops[i]), color='#9aa1ad', width=1.2, dash=True)
        d.actor(100, tops[i] + 40)
        d.text(100, tops[i] + 86, name, size=15, weight='m', maxw=176, blank='clave', accept=acc, minw=150)
    pos = {}
    for k, (lane, x, label, acc, opt) in acts.items():
        dy = opt.get('dy', 0)
        if opt.get('lab') == 'below':
            gy = tops[lane] + 36 + dy
            ly = gy + 46
        else:
            gy = tops[lane] + 88 + dy
            ly = gy - 56
        pos[k] = (x, gy)
        d.gear(x, gy)
        d.text(x, ly, label, size=15, weight='m', maxw=190, blank='clave', accept=acc, minw=150)

    def anchor(k, side, off):
        x, gy = pos[k]
        return {'r': (x + 27, gy + off), 'l': (x - 27, gy + off), 't': (x + off, gy - 17), 'b': (x + off, gy + 17)}[side]

    for a, sa, b, sb, oa, ob in arrows:
        p, q = anchor(a, sa, oa), anchor(b, sb, ob)
        if sa in 'tb' and sb in 'lr':
            d.arrow(p, q, via=[(p[0], q[1])])
        elif sa in 'lr' and sb in 'tb':
            d.arrow(p, q, via=[(q[0], p[1])])
        else:
            d.arrow(p, q)
    done(d)


L = 128
flujo('b3-01-flujo-requisitos', 'Flujo de trabajo de Requisitos', 10,
      [('Analista de sistemas', ['Analista de Sistemas'], L), ('Arquitecto', None, L),
       ('Especificador de casos de uso', ['Especificador de CU', 'Especificador de caso de uso'], L),
       ('Diseñador de interfaz de usuario', ['Diseñador de interfaces', 'Diseñador de IU', 'Diseñador de interfaz'], L)],
      {'enc': (0, 300, 'Encontrar actores y casos de uso', ['Encontrar actores y CU', 'Buscar actores y casos de uso'], {}),
       'est': (0, 860, 'Estructurar el modelo de casos de uso', ['Estructurar el modelo de CU', 'Estructurar modelo de casos de uso'], {}),
       'pri': (1, 450, 'Priorizar los casos de uso', ['Priorizar casos de uso', 'Priorizar CU'], {}),
       'det': (2, 610, 'Detallar un caso de uso', ['Detallar casos de uso', 'Detallar caso de uso', 'Detallar CU'], {}),
       'pro': (3, 770, 'Prototipar la interfaz de usuario', ['Prototipar interfaz de usuario', 'Prototipar la UI', 'Prototipar interfaces', 'Prototipar IU'], {})},
      [('enc', 'b', 'pri', 'l', 0, 0), ('pri', 'b', 'det', 'l', 0, 0), ('det', 'b', 'pro', 'l', 0, 0), ('det', 'r', 'est', 'b', 0, 0)],
      'PUDS, fig. 7.10 · Celina, pág. 75 · Parcial 2024, P3')

flujo('b3-02-flujo-analisis', 'Flujo de trabajo de Análisis', 20,
      [('Arquitecto', None, L), ('Ingeniero de casos de uso', ['Ingeniero de CU'], L), ('Ingeniero de componentes', None, L)],
      {'arq': (0, 300, 'Análisis de la arquitectura', ['Analizar la arquitectura'], {}),
       'cu': (1, 470, 'Analizar un caso de uso', ['Analizar los casos de uso', 'Análisis de casos de uso', 'Analizar CU'], {}),
       'cl': (2, 640, 'Analizar una clase', ['Análisis de clases', 'Analizar clase'], {}),
       'pa': (2, 860, 'Analizar un paquete', ['Análisis de paquetes', 'Analizar paquete'], {})},
      [('arq', 'b', 'cu', 'l', 0, 0), ('cu', 'b', 'cl', 'l', 0, 0), ('cl', 'r', 'pa', 'l', 0, 0)],
      'PUDS, fig. 8.18 · Celina, pág. 88 · Simulación 2024 A, P1')

flujo('b3-03-flujo-diseno', 'Flujo de trabajo de Diseño', 30,
      [('Arquitecto', None, L), ('Ingeniero de casos de uso', ['Ingeniero de CU'], L), ('Ingeniero de componentes', None, L)],
      {'arq': (0, 300, 'Diseño de la arquitectura', ['Diseño arquitectónico', 'Diseñar la arquitectura'], {}),
       'cu': (1, 660, 'Diseñar un caso de uso', ['Diseño de un caso de uso', 'Diseñar caso de uso', 'Diseñar CU'], {}),
       'cl': (2, 480, 'Diseñar una clase', ['Diseño de una clase', 'Diseñar clase'], {}),
       'su': (2, 870, 'Diseñar un subsistema', ['Diseño de un subsistema', 'Diseñar subsistema'], {})},
      [('arq', 'b', 'cu', 'l', 8, 0), ('arq', 'b', 'cl', 'l', -8, 0), ('cl', 'r', 'cu', 'b', -9, -9), ('cl', 'r', 'su', 'l', 9, 9), ('cu', 'b', 'su', 'l', 9, -5)],
      'PUDS, fig. 9.16 · Celina, pág. 100 · Recuperatorio 2024, P6')

flujo('b3-04-flujo-implementacion', 'Flujo de trabajo de Implementación', 40,
      [('Arquitecto', None, L), ('Integrador de sistemas', ['Integrador de sistema', 'Integrador del sistema'], L), ('Ingeniero de componentes', None, 236)],
      {'arq': (0, 300, 'Implementación de la arquitectura', ['Implementar la arquitectura'], {}),
       'int': (1, 440, 'Integrar sistemas', ['Integrar sistema', 'Integrar el sistema'], {}),
       'cl': (2, 680, 'Implementar una clase', ['Implementar clase'], {}),
       'su': (2, 440, 'Implementar un subsistema', ['Implementar subsistema'], {'lab': 'below', 'dy': 110}),
       'pu': (2, 880, 'Realizar prueba de unidad', ['Realizar prueba unitaria', 'Prueba de unidad', 'Prueba unitaria'], {'lab': 'below', 'dy': 110})},
      [('arq', 'b', 'int', 'l', 0, 0), ('int', 'b', 'cl', 'l', 9, 0), ('int', 'b', 'su', 't', -9, -9), ('su', 'r', 'cl', 'b', -9, 0), ('su', 'r', 'pu', 'l', 9, 9), ('cl', 'r', 'pu', 't', 0, 0)],
      'PUDS, cap. 10 · Celina, pág. 113')

flujo('b3-05-flujo-prueba', 'Flujo de trabajo de Prueba', 50,
      [('Ingeniero de pruebas', ['Diseñador de pruebas'], L), ('Ingeniero de pruebas de integración', None, L),
       ('Ingeniero de pruebas de sistema', None, L), ('Ingeniero de componentes', None, L)],
      {'pl': (0, 290, 'Planificar prueba', ['Planear la prueba', 'Planificar la prueba'], {}),
       'di': (0, 470, 'Diseñar prueba', ['Diseñar la prueba'], {}),
       'ev': (0, 910, 'Evaluar prueba', ['Evaluar la prueba'], {}),
       'in': (1, 680, 'Realizar prueba de integración', ['Realizar pruebas de integración', 'Efectuar prueba de integración'], {}),
       'si': (2, 800, 'Realizar prueba de sistema', ['Realizar prueba del sistema', 'Efectuar prueba de sistema'], {}),
       'im': (3, 560, 'Implementar pruebas', ['Implementar prueba', 'Implementar la prueba'], {})},
      [('pl', 'r', 'di', 'l', 0, 0), ('di', 'b', 'im', 'l', 0, 0), ('im', 'r', 'in', 'b', -9, 0), ('im', 'r', 'si', 'b', 9, 0), ('in', 'r', 'ev', 'b', 0, -9), ('si', 'r', 'ev', 'b', 0, 9)],
      'PUDS, cap. 11 · Celina, pág. 123')

# ───────────────────────── B3 · Ciclo de vida: fases, flujos e hitos
d = Diagram('b3-06-ciclo-de-vida', 'Ciclo de vida: fases, flujos de trabajo e hitos', B3, 60, 1040, 550, 'PUDS, págs. 37 y 124 · Celina, págs. 64–67 · PF, pág. 130')
x0, cw, y0, rh = 230, 195, 78, 62
fases = [('Inicio', None), ('Elaboración', None), ('Construcción', None), ('Transición', None)]
d.text(x0 + 2 * cw, 20, 'Fases', size=14, weight='b', color=MUTED)
for i, (f, acc) in enumerate(fases):
    d.box(x0 + i * cw, 36, cw, 40, f, weight='b', fill=HEAD, r=0, blank='clave')
flujos = ['Requisitos', 'Análisis', 'Diseño', 'Implementación', 'Prueba']
inten = [[.75, .95, .35, .12], [.2, .9, .3, .05], [.12, .7, .6, .1], [.1, .3, .95, .3], [.06, .2, .6, .75]]
d.text(115, 56, 'Flujos de trabajo\nfundamentales', size=13, weight='b', color=MUTED)
for r, fl in enumerate(flujos):
    y = y0 + r * rh
    d.rect(x0, y, 4 * cw, rh, fill=BG, r=0, width=1)
    d.box(20, y + 9, 190, rh - 18, fl, weight='b', blank='clave')
    pts = [(x0, y + rh - 4)]
    xs = [x0 + cw * (i + .5) for i in range(4)]
    for i in range(4):
        pts.append((xs[i], y + rh - 4 - (rh - 14) * inten[r][i]))
    pts.append((x0 + 4 * cw, y + rh - 4))
    # curva suavizada
    sm = []
    for t in range(0, 101):
        u = t / 100 * (len(pts) - 1)
        i = min(int(u), len(pts) - 2)
        f = u - i
        f = f * f * (3 - 2 * f)
        sm.append(((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * (u - i)) * 2, (pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f) * 2))
    d.d.polygon(sm + [((x0 + 4 * cw) * 2, (y + rh - 4) * 2), (x0 * 2, (y + rh - 4) * 2)], fill='#c9d2f5')
    for i in range(1, 4):
        d.line((x0 + i * cw, y), (x0 + i * cw, y + rh), color='#9aa1ad', width=1)
yb = y0 + 5 * rh
d.text(115, yb + 24, 'Cada fase se divide en', size=13, color=MUTED)
d.text(115, yb + 48, 'iteraciones', size=15, weight='b', blank='clave', accept=['iteración'], minw=150)
for i in range(4):
    for k in range(2 if i in (0, 3) else 3):
        n = 2 if i in (0, 3) else 3
        d.rect(x0 + i * cw + 8 + k * (cw - 16) / n, yb + 10, (cw - 16) / n - 6, 26, fill=SOFT, r=4, width=1)
        d.text(x0 + i * cw + 8 + k * (cw - 16) / n + ((cw - 16) / n - 6) / 2, yb + 23, 'iter.', size=11, color=MUTED)
d.text(115, yb + 92, 'Hito con el que\ntermina la fase', size=13, weight='b', color=MUTED)
hitos = [('Objetivos del ciclo de vida', ['Objetivos del CV']), ('Arquitectura del ciclo de vida', ['Arquitectura del CV', 'Línea base de la arquitectura']),
         ('Capacidad operativa inicial', None), ('Lanzamiento del producto', ['Release del producto', 'Lanzamiento'])]
for i, (hname, acc) in enumerate(hitos):
    d.box(x0 + i * cw + 6, yb + 62, cw - 12, 60, hname, size=14, blank='clave', accept=acc)
done(d)

# ───────────────────────── B3 · Modelos y dependencias
d = Diagram('b3-07-modelos', 'Modelos del Proceso Unificado y su relación con los casos de uso', B3, 70, 980, 430, 'PUDS, cap. 1 (modelos del PU) · Celina, págs. 64–65')
cu = d.box(40, 180, 230, 60, 'Modelo de casos de uso', weight='b', fill=HEAD, blank='clave', accept=['Modelo de CU'])
ms = [('Modelo de análisis', 'especificado por'), ('Modelo de diseño', 'realizado por'), ('Modelo de despliegue', 'distribuido por'),
      ('Modelo de implementación', 'implementado por'), ('Modelo de prueba', 'verificado por')]
for i, (m, rel) in enumerate(ms):
    y = 22 + i * 76
    b = d.box(690, y, 250, 52, m, weight='b', blank='clave', accept=[m.replace('Modelo de ', '')])
    d.arrow(left(b), (270, 195 + i * 8), dash=True)
    d.text(480, 121.5 + 42 * i, rel, size=14, weight='m', blank='extra', minw=150, bg=BG)
d.note(40, 290, 'Todos los modelos siguen la traza\nhasta el modelo de casos de uso:\npor eso el proceso está «dirigido\npor casos de uso».', size=13)
done(d)

# ───────────────────────── B3 · Análisis vs. Diseño
d = Diagram('b3-08-analisis-vs-diseno', 'Modelo de análisis vs. modelo de diseño', B3, 80, 980, 470, 'PUDS, tabla 9.1 · Celina, págs. 93–94 · Simulación 2024 B, P9 y P11')
d.table(20, 20, [250, 345, 345], [
    ['', 'Modelo de análisis', 'Modelo de diseño'],
    ['Qué clase de modelo es', ('Conceptual', 'clave', ['Modelo conceptual']), ('Físico', 'clave', ['Modelo físico'])],
    ['Respecto de la implementación', ('Genérico', 'clave'), ('Específico', 'clave', ['No genérico'])],
    ['Estereotipos de las clases', ('Tres: entidad, control e interfaz', 'clave', ['Tres', 'entidad, control e interfaz', 'entidad, control y frontera', 'Tres: entidad, control y frontera']), ('Cualquier número, según el lenguaje', 'clave', ['Cualquier número'])],
    ['Formalidad', ('Menos formal', 'clave'), ('Más formal', 'clave')],
    ['Dinámica', ('Poco centrado en la secuencia', 'extra', ['No muy centrado en la secuencia']), ('Muy centrado en la secuencia', 'extra')],
    ['Mantenimiento en el ciclo de vida', ('Puede no mantenerse', 'clave', ['Puede no estar mantenido']), ('Debe mantenerse', 'clave', ['Debe ser mantenido'])],
    ['Papel', ('Bosquejo del diseño', 'extra', ['Bosquejo']), ('Manifiesto del diseño', 'extra', ['Manifiesto'])],
], rowh=[44, 50, 50, 60, 50, 50, 56, 50])
done(d)

# ───────────────────────── B2 · Estructuras de Bass
d = Diagram('b2-01-estructuras', 'Las tres estructuras de una arquitectura (Bass)', B2, 10, 1040, 420, 'Bass et al., cap. 1 · Celina, págs. 20–22 · Parcial 2024, P9 · Recuperatorio 2024, P10')
d.table(20, 20, [200, 270, 270, 270], [
    ['', ('Módulos', 'clave', ['Estructuras de módulos']), ('Componentes y conectores', 'clave', ['C&C', 'Componentes y conectores (C&C)']), ('Asignación', 'clave', ['Estructuras de asignación', 'Allocation'])],
    ['Qué muestra', 'Unidades de implementación: visión estática', 'El sistema en tiempo de ejecución y cómo interactúan sus partes', 'Cómo se relaciona el software con lo que no es software'],
    ['Elementos', 'Clases, paquetes, capas', 'Servicios, clientes, servidores, filtros, procesos', 'Procesadores, archivos y directorios, equipos'],
    ['Estructuras típicas', ('Descomposición, usos, capas, clases', 'extra', ['Descomposición, usos, capas y clases']), ('Servicios y concurrencia', 'extra', ['Servicios, concurrencia']), ('Despliegue, implementación y asignación de trabajo', 'extra', ['Despliegue, implementación, asignación de trabajo'])],
    ['Pregunta que responde', '¿Qué otros elementos de software puede usar un módulo?', '¿Qué partes del sistema pueden funcionar en paralelo?', '¿En qué procesador se ejecuta cada elemento del software?'],
], rowh=[46, 74, 74, 82, 86], size=14)
done(d)

# ───────────────────────── B2 · Escenario de atributo de calidad
d = Diagram('b2-02-escenario-calidad', 'Las seis partes de un escenario de atributo de calidad', B2, 20, 1040, 330, 'Bass et al., fig. 3.1 · Celina, págs. 26–27 · PF, pág. 49')
fu = d.box(30, 120, 180, 70, 'Fuente del estímulo', weight='b', blank='clave', accept=['Fuente de estímulo', 'Fuente'])
env = d.rect(400, 50, 270, 215, fill='#f5f6fa', r=14)
d.text(535, 78, 'Entorno', size=16, weight='b', blank='clave', accept=['Ambiente'], minw=140)
ar = d.box(445, 125, 180, 70, 'Artefacto', weight='b', fill=HEAD, blank='clave')
d.note(535, 230, 'estado del sistema cuando\nllega el estímulo', anchor='mm', size=12)
me = d.box(840, 120, 180, 70, 'Medida de la respuesta', weight='b', blank='clave', accept=['Medida de respuesta', 'Medida'])
d.arrow(right(fu), (445, 160))
d.text(308, 138, 'Estímulo', size=16, weight='b', blank='clave', minw=120)
d.arrow((625, 160), left(me))
d.text(735, 138, 'Respuesta', size=16, weight='b', blank='clave', minw=120)
d.note(120, 215, 'quién o qué lo genera', anchor='mm', size=12)
d.note(308, 185, 'evento que llega\nal sistema', anchor='mm', size=12)
d.note(735, 185, 'actividad que\nresulta', anchor='mm', size=12)
d.note(930, 215, 'cómo se comprueba\nque se cumplió', anchor='mm', size=12)
done(d)


def arbol(file, title, order, raiz, entra, sale, ramas, fuente, h=None, colw=None):
    """Árbol de tácticas: categorías en columnas y tácticas debajo."""
    n = len(ramas)
    w = 1040
    colw = colw or (w - 40) / n
    filas = max(len(r[1]) for r in ramas)
    h = h or 190 + filas * 46 + 30
    d = Diagram(file, title, B2, order, w, h, fuente)
    rb = d.box(w / 2 - 170, 18, 340, 46, raiz, weight='b', fill=HEAD)
    d.arrow((60, 41), left(rb))
    d.text(100, 22, entra, size=13, color=MUTED)
    d.arrow(right(rb), (w - 60, 41))
    d.text(w - 110, 16, sale, size=12, color=MUTED)
    for i, (cat, tacs, lvl) in enumerate(ramas):
        cx = 20 + colw * i + colw / 2
        cb = d.box(cx - colw / 2 + 12, 100, colw - 24, 54, cat, weight='b', blank='clave', accept=lvl)
        d.arrow(bottom(rb), top(cb), head='none')
        for k, t in enumerate(tacs):
            txt, tl, acc = (t, 'extra', None) if isinstance(t, str) else (t + (None,))[:3]
            if tl == 'fijo':
                d.text(cx, 190 + k * 46, txt, size=13, weight='b', color=MUTED, maxw=colw - 30)
            else:
                d.box(cx - colw / 2 + 24, 172 + k * 46, colw - 48, 38, txt, size=14, weight='r', fill=BG, blank=tl, accept=acc)
    done(d)


arbol('b2-03-tacticas-modificabilidad', 'Tácticas de modificabilidad', 30, 'Tácticas para controlar la modificabilidad', 'Llega un cambio', 'Cambio hecho,\nprobado y desplegado',
      [('Aumentar la cohesión', [('Dividir el módulo', 'clave', ['Dividir módulo', 'Dividir un módulo']), ('Redistribuir responsabilidades', 'clave')], None),
       ('Reducir el acoplamiento', [('Encapsular', 'clave'), ('Usar un intermediario', 'clave', ['Intermediario']), ('Abstraer servicios comunes', 'clave'), ('Restringir dependencias', 'clave')], None),
       ('Aplazar la vinculación', [('Reemplazo de componentes', 'extra'), ('Parametrización en compilación', 'extra', ['Parametrización en tiempo de compilación']), ('Vinculación en configuración', 'extra', ['Vinculación en tiempo de configuración']), ('Archivos de recursos', 'extra'), ('Descubrimiento', 'extra'), ('Polimorfismo', 'extra')], ['Diferir el enlace', 'Diferir enlace', 'Aplazar el momento de vinculación'])],
      'Bass et al., cap. de modificabilidad · Celina, págs. 32–33 · PF, págs. 54–55')

arbol('b2-04-tacticas-rendimiento', 'Tácticas de rendimiento (performance)', 40, 'Tácticas para controlar el rendimiento', 'Llega un evento', 'Respuesta dentro del\ntiempo y los recursos',
      [('Controlar la demanda de recursos', [('Gestionar las solicitudes de trabajo', 'clave', ['Gestionar solicitudes de trabajo']), ('Limitar la respuesta a eventos', 'extra'), ('Priorizar eventos', 'clave'), ('Reducir la sobrecarga computacional', 'clave', ['Reducir sobrecarga computacional']), ('Limitar los tiempos de ejecución', 'extra'), ('Aumentar la eficiencia en el uso de recursos', 'extra', ['Aumentar la eficiencia'])], ['Controlar la demanda', 'Control de la demanda de recursos']),
       ('Gestionar los recursos', [('Aumentar los recursos', 'clave', ['Aumentar recursos']), ('Introducir concurrencia', 'clave'), ('Mantener múltiples copias de los cálculos', 'clave', ['Múltiples copias de los cálculos']), ('Mantener múltiples copias de los datos', 'clave', ['Múltiples copias de los datos', 'Replicación y caché de datos']), ('Limitar el tamaño de las colas', 'extra'), ('Programar los recursos', 'extra', ['Planificar los recursos'])], ['Gestionar los recursos disponibles', 'Gestión de recursos'])],
      'Bass et al., cap. de performance · Celina, págs. 36–38 · PF, págs. 63–66')

# ───────────────────────── B2 · Vistas 4+1
d = Diagram('b2-05-vistas-4mas1', 'Modelo de vistas 4+1 (Kruchten)', B2, 50, 1000, 500, 'Sommerville, cap. 6 · Celina, pág. 42 · PF, págs. 33–34')
c = d.box(390, 190, 220, 80, 'Escenarios\n(casos de uso)', weight='b', fill=HEAD, blank='clave', answer='Escenarios', accept=['Casos de uso', 'Escenarios o casos de uso', 'Escenarios (casos de uso)'])
vs = [(60, 50, 'Vista lógica', 'Abstracciones clave del sistema: objetos y clases. Se relaciona con los requisitos.', ['Lógica']),
      (640, 50, 'Vista de procesos', 'Cómo se compone el sistema de procesos en tiempo de ejecución. Rendimiento y disponibilidad.', ['Procesos', 'Vista de proceso']),
      (60, 300, 'Vista de desarrollo', 'Cómo se descompone el software para desarrollarlo: módulos, capas, librerías.', ['Desarrollo']),
      (640, 300, 'Vista física', 'Hardware y cómo se distribuyen los componentes en los procesadores.', ['Física', 'Vista de despliegue'])]
for x, y, n, desc, acc in vs:
    d.rect(x, y, 300, 130, fill=BG)
    b = d.box(x, y, 300, 44, n, weight='b', blank='clave', accept=acc, r=8)
    d.text(x + 150, y + 88, desc, size=13, color=MUTED, maxw=270)
    cx, cy = x + 150, y + 65
    tx = 390 if x < 300 else 610
    ty = 205 if y < 200 else 255
    d.arrow((x + 300 if x < 300 else x, y + 110 if y < 200 else y + 20), (tx, ty), head='none', dash=True)
d.note(500, 456, 'Las cuatro vistas se vinculan mediante escenarios comunes. Es la organización que usa el Proceso Unificado.', anchor='mm', size=13)
done(d)

# ───────────────────────── B2 · Capas
d = Diagram('b2-06-capas', 'Arquitectura en capas genérica', B2, 60, 900, 400, 'Sommerville, fig. 6.8 · Celina, pág. 45 · PF, págs. 69–74')
caps = [('Interfaz de usuario', ['Presentación', 'Capa de presentación']),
        ('Gestión de la interfaz de usuario · Autenticación y autorización', ['Gestión de interfaz de usuario', 'Autenticación y autorización', 'Gestión de la interfaz de usuario, autenticación y autorización']),
        ('Lógica de negocio · Funcionalidad de la aplicación', ['Lógica de negocio', 'Lógica empresarial', 'Funcionalidad de la aplicación', 'Lógica del negocio']),
        ('Soporte del sistema: sistema operativo, base de datos', ['Soporte del sistema', 'Soporte del sistema (SO, base de datos)'])]
for i, (cname, acc) in enumerate(caps):
    d.box(60, 30 + i * 78, 560, 62, cname, weight='b', fill=HEAD if i == 0 else SOFT, blank='clave', accept=acc, r=4)
    if i < 3:
        d.arrow((340, 92 + i * 78), (340, 108 + i * 78))
d.arrow((700, 40), (700, 320))
d.text(790, 150, 'Cada capa depende solo', size=13, color=MUTED)
d.text(790, 172, 'de la capa inmediatamente', size=13, color=MUTED)
d.text(790, 198, 'inferior', size=15, weight='b', blank='clave', accept=['de abajo'], minw=120)
d.text(790, 240, 'Atributo que favorece:', size=13, color=MUTED)
d.text(790, 266, 'Modificabilidad', size=15, weight='b', blank='clave', accept=['Modificabilidad y portabilidad', 'Mantenibilidad'], minw=150)
done(d)

# ───────────────────────── B2 · SOA
d = Diagram('b2-07-soa', 'Arquitectura orientada a servicios (SOA)', B2, 70, 1040, 430, 'Sommerville, fig. 18.2 · Celina, págs. 58–60 · PF, págs. 106–109')
reg = d.box(205, 30, 240, 62, 'Registro de servicios', weight='b', fill=HEAD, blank='clave', accept=['Registro', 'Registro de servicio'])
sol = d.box(30, 250, 240, 62, 'Solicitante del servicio', weight='b', blank='clave', accept=['Solicitante', 'Solicitante de servicios', 'Cliente del servicio'])
pro = d.box(380, 250, 240, 62, 'Proveedor del servicio', weight='b', blank='clave', accept=['Proveedor', 'Proveedor de servicios'])
d.arrow(top(sol), at(reg, .25, 1))
d.arrow(top(pro), at(reg, .75, 1))
d.arrow(right(sol), left(pro))
d.text(125, 165, 'Encontrar', size=15, weight='m', blank='clave', accept=['Buscar', 'Find', 'Descubrir'], minw=120)
d.text(525, 165, 'Publicar', size=15, weight='m', blank='clave', accept=['Publish'], minw=120)
d.text(325, 335, 'Enlazar (SOAP)', size=15, weight='m', blank='clave', answer='Enlazar', accept=['Bind', 'Vincular', 'Enlazar (SOAP)'], minw=150)
d.note(500, 330, 'ofrece el servicio', anchor='mm')
d.table(680, 60, [120, 220], [
    ['Estándar', 'Para qué sirve'],
    [('SOAP', 'clave'), 'Intercambio de mensajes entre servicios'],
    [('WSDL', 'clave'), 'Definición de la interfaz del servicio'],
    [('WS-BPEL', 'extra', ['BPEL']), 'Lenguaje de flujo de trabajo para componer servicios'],
    [('UDDI', 'extra'), 'Descubrimiento de servicios (en desuso)'],
], rowh=[40, 58, 58, 66, 58], size=14)
done(d)

# ───────────────────────── B2 · Microservicios
d = Diagram('b2-08-microservicios', 'Topología de una arquitectura de microservicios', B2, 80, 1040, 460, 'Richards y Ford (Word de la cátedra, pág. 134) · PF, pág. 112 · Celina, págs. 60–61 · Simulación 2024 A, P4')
for i in range(3):
    b = d.box(230 + i * 200, 20, 170, 46, 'Peticiones del cliente', size=14, blank='extra' if i == 0 else None, accept=['Client requests', 'Clientes', 'Peticiones de clientes'])
    d.arrow(bottom(b), (b[0] + b[2] / 2, 100))
api = d.rect(60, 100, 920, 62, fill=HEAD, r=6)
d.text(520, 131, 'Capa de API', size=17, weight='b', blank='clave', accept=['API Layer', 'API Gateway', 'Capa API', 'Puerta de enlace'], minw=170)
for i in range(5):
    x = 60 + i * 187
    d.arrow((x + 85, 162), (x + 85, 196))
    d.rect(x, 196, 172, 200, fill='#f5f6fa', r=8)
    if i == 0:
        d.text(x + 86, 220, 'Servicio', size=16, weight='b', blank='clave', accept=['Microservicio', 'Service'], minw=130)
        d.box(x + 26, 244, 120, 30, 'Módulo', size=13, fill=BG, blank='extra', accept=['Module', 'Módulos'])
    else:
        d.text(x + 86, 220, 'Servicio', size=16, weight='b')
        d.box(x + 26, 244, 120, 30, 'Módulo', size=13, fill=BG)
    d.box(x + 26, 280, 120, 30, 'Módulo', size=13, fill=BG)
    d.arrow((x + 86, 310), (x + 86, 334))
    d.box(x + 16, 334, 140, 44, 'Base de datos', size=14, fill=SOFT, r=20, blank='clave' if i == 0 else None, accept=['Database', 'BD', 'Base de datos propia'])
d.note(520, 420, 'Cada servicio modela un contexto delimitado: incluye sus módulos y su propia base de datos.', anchor='mm')
done(d)

# ───────────────────────── B2 · Patrones distribuidos
d = Diagram('b2-09-patrones-distribuidos', 'Patrones arquitectónicos para sistemas distribuidos', B2, 90, 1040, 440, 'Sommerville, cap. 17 · Celina, págs. 53–58 · PF, págs. 91–105')
d.table(20, 20, [270, 440, 290], [
    ['Patrón', 'Idea central', 'Cuándo se usa'],
    [('Maestro-esclavo', 'clave', ['Maestro esclavo', 'Master-slave']), 'El maestro se encarga del cómputo, la coordinación y las comunicaciones, y controla a los esclavos, dedicados a acciones específicas.', 'Sistemas de tiempo real con tiempos de respuesta garantizados'],
    [('Cliente-servidor de dos niveles', 'clave', ['Cliente servidor de dos niveles', 'Cliente-servidor dos niveles']), 'Un servidor lógico y muchos clientes. Cliente liviano: solo presentación. Cliente pesado: también procesa.', 'Sistemas simples o cuando conviene centralizar por seguridad'],
    [('Cliente-servidor multinivel', 'clave', ['Cliente servidor multinivel', 'Multinivel', 'Multi-tier']), 'Presentación, procesamiento, gestión de datos y base de datos corren como procesos separados.', 'Alto volumen de transacciones en el servidor'],
    [('Componentes distribuidos', 'clave', ['Objetos distribuidos']), 'Componentes que ofrecen servicios por su interfaz y se llaman entre sí a través de middleware.', 'Combinar recursos de distintos sistemas y bases de datos'],
    [('Peer-to-peer (P2P)', 'clave', ['P2P', 'Peer to peer', 'De igual a igual', 'Peer-to-peer']), 'Descentralizado: cualquier nodo puede calcular; no hay distinción entre cliente y servidor.', 'Intercambio de información local o muchos cómputos independientes'],
], rowh=[42, 78, 74, 68, 68, 68], size=14)
done(d)

# ───────────────────────── B4 · Clasificación GoF
d = Diagram('b4-01-clasificacion-gof', 'Catálogo GoF: propósito y alcance', B4, 10, 1040, 520, 'GoF, tabla 1.1 · Celina, pág. 132 · Parcial 2024 P6 · Recuperatorio 2024 P3 · Simulación 2024 A P20')
X = [150, 440, 730]
CW = 290
d.text(X[0] + 1.5 * CW, 18, 'Propósito', size=14, weight='b', color=MUTED)
for i, p in enumerate([('De creación', ['Creacional', 'Creacionales', 'Creación']), ('Estructural', ['Estructurales', 'De estructura']), ('De comportamiento', ['Comportamiento', 'Comportamental', 'Comportamentales'])]):
    d.box(X[i], 34, CW, 40, p[0], weight='b', fill=HEAD, r=0, blank='clave', accept=p[1])
d.text(60, 54, 'Alcance', size=14, weight='b', color=MUTED)
d.box(20, 74, 130, 80, 'Clase', weight='b', fill=SOFT, r=0, blank='clave', accept=['De clase'])
d.box(20, 154, 130, 340, 'Objeto', weight='b', fill=SOFT, r=0, blank='clave', accept=['De objeto'])
for i in range(3):
    d.rect(X[i], 74, CW, 80, fill=BG, r=0, width=1)
    d.rect(X[i], 154, CW, 340, fill=BG, r=0, width=1)
VISTOS = {'Factory Method', 'Abstract Factory', 'Singleton', 'Adapter (de clases)', 'Adapter (de objetos)', 'Composite', 'Facade', 'Proxy', 'Interpreter', 'Template Method', 'Iterator', 'Observer', 'State', 'Strategy'}
cells = {(0, 0): ['Factory Method'], (1, 0): ['Adapter (de clases)'], (2, 0): ['Interpreter', 'Template Method'],
         (0, 1): ['Abstract Factory', 'Builder', 'Prototype', 'Singleton'],
         (1, 1): ['Adapter (de objetos)', 'Bridge', 'Composite', 'Decorator', 'Facade', 'Flyweight', 'Proxy'],
         (2, 1): ['Chain of Responsibility', 'Command', 'Iterator', 'Mediator', 'Memento', 'Observer', 'State', 'Strategy', 'Visitor']}
for (ci, ri), ps in cells.items():
    y = 82 if ri == 0 else 162
    for k, p in enumerate(ps):
        base = p.split(' (')[0]
        acc = [base] if '(' in p else None
        if base == 'Chain of Responsibility':
            acc = ['Chain of Responsability', 'Cadena de responsabilidad']
        d.box(X[ci] + 18, y + k * 36, CW - 36, 31, p, size=14, weight='r', fill=BG, r=4, blank='clave' if p in VISTOS else 'extra', accept=acc)
done(d)


# ───────────────────────── B4 · Estructuras de patrones
def gof(file, title, order, w, h, fuente):
    return Diagram(file, title, B4, order, w, h, fuente)


d = gof('b4-02-factory-method', 'Estructura de Factory Method', 20, 900, 380, 'GoF, pág. 211 (estructura) · Celina, págs. 133–134')
pr = d.uml(60, 40, 220, 'Product', accept=['Producto'], abstract=True)
cp = d.uml(60, 240, 220, 'ConcreteProduct', accept=['ProductoConcreto', 'Producto concreto', 'ConcretProduct'])
cr = d.uml(520, 40, 300, 'Creator', ['FactoryMethod()', 'AnOperation()'], accept=['Creador'], abstract=True)
cc = d.uml(520, 240, 300, 'ConcreteCreator', ['FactoryMethod()'], accept=['CreadorConcreto', 'Creador concreto', 'ConcretCreator'])
d.arrow(top(cp), bottom(pr), head='tri')
d.arrow(top(cc), bottom(cr), head='tri')
d.arrow(left(cc), right(cp), dash=True)
d.note(400, 248, '«crea»', anchor='mm')
d.note(520, 150, 'AnOperation() llama a FactoryMethod();\nla subclase decide qué producto crear.', size=12)
done(d)

d = gof('b4-03-abstract-factory', 'Estructura de Abstract Factory', 30, 1040, 460, 'GoF, pág. 125 (estructura) · Celina, págs. 135–136 · PF, págs. 305–307')
af = d.uml(40, 40, 300, 'AbstractFactory', ['CreateProductA()', 'CreateProductB()'], accept=['FábricaAbstracta', 'Fábrica abstracta'], abstract=True)
f1 = d.uml(20, 250, 200, 'ConcreteFactory1', ['CreateProductA()', 'CreateProductB()'], accept=['ConcreteFactory', 'FábricaConcreta', 'Fábrica concreta'])
f2 = d.uml(240, 250, 200, 'ConcreteFactory2', ['CreateProductA()', 'CreateProductB()'], blank=None)
cl = d.uml(820, 40, 180, 'Client', accept=['Cliente'])
pa = d.uml(540, 130, 200, 'AbstractProductA', accept=['AbstractProduct', 'ProductoAbstracto', 'Producto abstracto', 'ProductoAbstractoA'], abstract=True)
a1 = d.uml(480, 230, 150, 'ProductA1', accept=['ConcreteProduct', 'ProductoConcreto', 'Producto concreto', 'ProductoA1'])
a2 = d.uml(650, 230, 150, 'ProductA2', blank=None)
pb = d.uml(540, 320, 200, 'AbstractProductB', blank=None, abstract=True)
b1 = d.uml(480, 405, 150, 'ProductB1', blank=None, hname=34)
b2 = d.uml(650, 405, 150, 'ProductB2', blank=None, hname=34)
for s, t in ((f1, af), (f2, af), (a1, pa), (a2, pa), (b1, pb), (b2, pb)):
    d.arrow(top(s), (t[0] + t[2] / 2 + (-40 if s in (f1, a1, b1) else 40), t[1] + t[3]), head='tri')
d.arrow(left(cl), right(af))
d.arrow(bottom(cl), (910, 150), head='none')
d.arrow((910, 150), right(pa))
d.arrow((910, 150), (910, 340), head='none')
d.arrow((910, 340), right(pb))
d.note(830, 410, 'Cada fábrica concreta crea\nuna familia de productos\nrelacionados.', size=12)
done(d)

d = gof('b4-04-adapter', 'Estructura de Adapter (de objetos)', 40, 940, 340, 'GoF, págs. 133–135 · Celina, págs. 136–137 · PF, págs. 300–301')
cl = d.uml(30, 50, 170, 'Client', accept=['Cliente'])
tg = d.uml(300, 50, 230, 'Target', ['Request()'], accept=['Objetivo'], abstract=True)
ad = d.uml(300, 220, 230, 'Adapter', ['Request()'], accept=['Adaptador'])
ae = d.uml(660, 220, 240, 'Adaptee', ['SpecificRequest()'], accept=['Adaptado', 'Adaptable'])
d.arrow(right(cl), (300, 70))
d.arrow(top(ad), bottom(tg), head='tri')
d.arrow(at(ad, 1, .3), at(ae, 0, .3))
d.note(545, 222, 'adaptee', anchor='lm', size=12)
d.note(660, 110, 'Request() llama a\nadaptee.SpecificRequest()', size=12)
d.note(30, 250, 'En la variante de clases,\nAdapter hereda de Target\ny de Adaptee.', size=12)
done(d)

d = gof('b4-05-composite', 'Estructura de Composite', 50, 940, 400, 'GoF, págs. 182–184 · Celina, págs. 138–139 · PF, págs. 310–312')
cl = d.uml(30, 60, 160, 'Client', accept=['Cliente'])
co = d.uml(330, 30, 300, 'Component', ['Operation()', 'Add(Component)', 'Remove(Component)', 'GetChild(int)'], accept=['Componente'], abstract=True)
lf = d.uml(200, 280, 200, 'Leaf', ['Operation()'], accept=['Hoja'])
cm = d.uml(540, 280, 300, 'Composite', ['Operation()', 'Add(Component)', 'Remove(Component)'], accept=['Compuesto'])
d.arrow(right(cl), (330, 80))
d.arrow(top(lf), (430, co[1] + co[3]), head='tri')
d.arrow(top(cm), (560, co[1] + co[3]), head='tri')
d.arrow(at(cm, 1, .2), (630, 60), tail='diamond', via=[(890, cm[1] + cm[3] * .2), (890, 60)])
d.text(820, 42, 'hijos', size=14, weight='m', blank='extra', accept=['children', 'componentes', 'hijo'], minw=100)
d.note(30, 200, 'El cliente trata igual\na las hojas y a los\ncompuestos.', size=12)
done(d)

d = gof('b4-06-observer', 'Estructura de Observer', 60, 960, 400, 'GoF, págs. 278–280 · Celina, págs. 143–144 · PF, págs. 302–303')
su = d.uml(60, 40, 300, 'Subject', ['Attach(Observer)', 'Detach(Observer)', 'Notify()'], accept=['Sujeto'], abstract=True)
ob = d.uml(600, 40, 280, 'Observer', ['Update()'], accept=['Observador'], abstract=True)
cs = d.uml(60, 280, 300, 'ConcreteSubject', ['GetState()', 'SetState()'], accept=['SujetoConcreto', 'Sujeto concreto'])
cob = d.uml(600, 280, 280, 'ConcreteObserver', ['Update()'], accept=['ObservadorConcreto', 'Observador concreto'])
d.arrow(at(su, 1, .25), at(ob, 0, .25))
d.note(480, 38, 'observadores', anchor='mm', size=12)
d.arrow(top(cs), bottom(su), head='tri')
d.arrow(top(cob), bottom(ob), head='tri')
d.arrow(left(cob), right(cs))
d.note(480, 300, 'sujeto', anchor='mm', size=12)
d.note(400, 165, 'Notify() llama a Update()\nde cada observador.', size=12)
done(d)

d = gof('b4-07-strategy', 'Estructura de Strategy', 70, 980, 360, 'GoF, págs. 323–325 · Copia de Apunte Diseño, págs. 198–200 · PF, págs. 308–309 · Simulación 2024 B, P8')
cx = d.uml(40, 50, 260, 'Context', ['ContextInterface()'], accept=['Contexto'])
st = d.uml(520, 50, 300, 'Strategy', ['AlgorithmInterface()'], accept=['Estrategia'], abstract=True)
d.arrow(at(cx, 1, .3), at(st, 0, .3), tail='diamond')
d.note(410, 48, 'estrategia', anchor='mm', size=12)
for i, n in enumerate(['ConcreteStrategyA', 'ConcreteStrategyB', 'ConcreteStrategyC']):
    b = d.uml(360 + i * 205, 240, 195, n, ['AlgorithmInterface()'], blank='clave' if i == 0 else None, accept=['ConcreteStrategy', 'EstrategiaConcreta', 'Estrategia concreta', 'EstrategiaConcretaA'])
    d.arrow(top(b), (st[0] + 60 + i * 90, st[1] + st[3]), head='tri')
d.note(40, 190, 'El cliente elige el algoritmo y lo\npuede cambiar: los algoritmos\nson intercambiables.', size=12)
done(d)

d = gof('b4-08-state', 'Estructura de State', 80, 980, 360, 'GoF, pág. 315 · Celina, págs. 142–143 · Parcial 2024, P2')
cx = d.uml(40, 50, 260, 'Context', ['Request()'], accept=['Contexto'])
st = d.uml(540, 50, 280, 'State', ['Handle()'], accept=['Estado'], abstract=True)
d.arrow(at(cx, 1, .3), at(st, 0, .3), tail='diamond')
d.note(420, 48, 'estado', anchor='mm', size=12)
for i, n in enumerate(['ConcreteStateA', 'ConcreteStateB']):
    b = d.uml(470 + i * 230, 240, 210, n, ['Handle()'], blank='clave' if i == 0 else None, accept=['ConcreteState', 'EstadoConcreto', 'Estado concreto', 'EstadoConcretoA'])
    d.arrow(top(b), (st[0] + 90 + i * 100, st[1] + st[3]), head='tri')
d.note(40, 170, 'Request() llama a estado.Handle().\nEl objeto parece cambiar de clase\ncuando cambia su estado interno.', size=12)
done(d)

d = gof('b4-09-proxy', 'Estructura de Proxy', 90, 940, 360, 'GoF, págs. 298–299 · Celina, págs. 140–141 · Recuperatorio 2024, P14')
cl = d.uml(30, 50, 160, 'Client', accept=['Cliente'])
sj = d.uml(380, 40, 260, 'Subject', ['Request()'], accept=['Sujeto'], abstract=True)
rs = d.uml(180, 240, 260, 'RealSubject', ['Request()'], accept=['SujetoReal', 'Sujeto real'])
px = d.uml(600, 240, 260, 'Proxy', ['Request()'])
d.arrow(right(cl), (380, 70))
d.arrow(top(rs), (460, sj[1] + sj[3]), head='tri')
d.arrow(top(px), (560, sj[1] + sj[3]), head='tri')
d.arrow(left(px), right(rs))
d.note(520, 248, 'sujetoReal', anchor='mm', size=12)
d.note(680, 110, 'El proxy controla el acceso al\nsujeto real: remoto, virtual\no de protección.', size=12)
done(d)

# ───────────────────────── B1 · SOLID
d = Diagram('b1-01-solid', 'Los cinco principios SOLID', B1, 10, 1000, 400, 'Celina, págs. 5–8 · PF, págs. 1–7')
d.table(20, 20, [70, 360, 530], [
    ['', 'Principio', 'Idea'],
    ['S', ('Responsabilidad única', 'clave', ['SRP', 'Single Responsibility Principle', 'Única responsabilidad', 'Principio de responsabilidad única']), 'Una clase debe tener una sola razón para cambiar.'],
    ['O', ('Abierto/Cerrado', 'clave', ['OCP', 'Open/Closed Principle', 'Abierto cerrado', 'Open Closed']), 'Abierta a la extensión, cerrada a la modificación.'],
    ['L', ('Sustitución de Liskov', 'clave', ['LSP', 'Liskov Substitution Principle', 'Liskov']), 'Donde se espera el tipo base debe poder usarse un subtipo sin sorpresas.'],
    ['I', ('Segregación de interfaces', 'clave', ['ISP', 'Interface Segregation Principle', 'Segregación de interfaz']), 'Los clientes no deben depender de interfaces que no usan.'],
    ['D', ('Inversión de dependencias', 'clave', ['DIP', 'Dependency Inversion Principle', 'Inversión de dependencia']), 'Depender de abstracciones, no de implementaciones concretas.'],
], rowh=[42, 62, 62, 62, 62, 62])
done(d)

# ───────────────────────── B1 · GRASP
d = Diagram('b1-02-grasp', 'Los nueve patrones GRASP y el problema que resuelven', B1, 20, 1040, 600, 'Larman · Celina, págs. 8–17 · PF, págs. 12–22')
d.table(20, 20, [690, 310], [
    ['¿Qué problema resuelve?', 'Patrón'],
    ['¿Quién crea una instancia de A? Quien la contiene, la registra o tiene los datos para inicializarla.', ('Creador', 'clave', ['Creator'])],
    ['¿A quién asignarle una responsabilidad? A la clase que tiene la información necesaria para cumplirla.', ('Experto en información', 'clave', ['Experto', 'Information Expert', 'Experto de la información'])],
    ['¿Cómo reducir las dependencias y el impacto de los cambios?', ('Bajo acoplamiento', 'clave', ['Low Coupling'])],
    ['¿Quién recibe y coordina un evento del sistema detrás de la interfaz de usuario?', ('Controlador', 'clave', ['Controller'])],
    ['¿Cómo mantener las clases enfocadas, comprensibles y manejables?', ('Alta cohesión', 'clave', ['High Cohesion'])],
    ['¿Cómo manejar alternativas según el tipo sin preguntar con if/else?', ('Polimorfismo', 'clave', ['Polymorphism'])],
    ['¿A quién asignar una responsabilidad cuando ninguna clase del dominio puede asumirla sin perder cohesión o acoplarse?', ('Fabricación pura', 'clave', ['Pure Fabrication'])],
    ['¿Cómo evitar el acoplamiento directo entre dos elementos? Con un objeto intermedio.', ('Indirección', 'clave', ['Indirection'])],
    ['¿Cómo evitar que las variaciones de unos elementos afecten a otros? Con una interfaz estable.', ('Variaciones protegidas', 'clave', ['Protected Variations'])],
], rowh=[42, 56, 56, 52, 56, 52, 52, 66, 56, 56], first_col_head=False, size=14)
done(d)

# ───────────────────────── B1 · Máquina de estados
d = Diagram('b1-03-maquina-de-estados', 'Notación de una máquina de estados', B1, 30, 1000, 300, 'UML · Apunte de Fidanza, págs. 46–52 · PF, págs. 8–11 y 23–25')
d.d.ellipse([60 * 2, 118 * 2, 84 * 2, 142 * 2], fill=LINE)
d.text(72, 170, 'Estado inicial', size=14, blank='clave', accept=['Inicial', 'Pseudoestado inicial'], minw=130)
s1 = d.box(190, 100, 180, 60, 'Estado A', weight='b', r=22, blank='extra', answer='Estado', accept=['Estado A'])
s2 = d.box(640, 100, 180, 60, 'Estado B', weight='b', r=22)
d.arrow((84, 130), left(s1))
d.arrow(right(s1), left(s2))
d.text(505, 60, 'Transición', size=13, color=MUTED)
d.text(430, 105, 'evento', size=15, weight='m', blank='clave', accept=['Evento', 'disparador'], minw=90)
d.text(505, 105, '[guarda]', size=15, weight='m', blank='clave', answer='guarda', accept=['[guarda]', 'condición', 'condición de guarda'], minw=90)
d.text(585, 105, '/ acción', size=15, weight='m', blank='clave', answer='acción', accept=['/ acción', 'accion', 'efecto'], minw=90)
d.d.ellipse([918 * 2, 116 * 2, 946 * 2, 144 * 2], outline=LINE, width=3)
d.d.ellipse([924 * 2, 122 * 2, 940 * 2, 138 * 2], fill=LINE)
d.arrow(right(s2), (918, 130))
d.text(932, 170, 'Estado final', size=14, blank='clave', accept=['Final'], minw=120)
d.note(500, 215, 'La transición se dispara cuando ocurre el evento y la guarda es verdadera; al dispararse se ejecuta la acción.', anchor='mm')
d.note(500, 245, 'Un estado compuesto contiene subestados; una transición automática no lleva evento.', anchor='mm')
done(d)

# ───────────────────────── B5 · Manifiesto
d = Diagram('b5-01-manifiesto-valores', 'Los cuatro valores del Manifiesto Ágil', B5, 10, 980, 320, 'Celina, pág. 146 · PF, pág. 316 · Parcial 2024, P4')
d.table(20, 20, [400, 140, 400], [
    ['Se valora más…', '', '…que'],
    [('Individuos e interacciones', 'clave', ['Individuos e interacción']), 'por sobre', ('Procesos y herramientas', 'clave')],
    [('Software funcionando', 'clave', ['Software que funciona']), 'por sobre', ('Extensa documentación', 'clave', ['Documentación extensa', 'Documentación exhaustiva'])],
    [('Colaboración del cliente', 'clave', ['Colaboración con el cliente']), 'por sobre', ('Negociación contractual', 'clave', ['Negociación de contratos'])],
    [('Responder al cambio', 'clave', ['Respuesta al cambio']), 'por sobre', ('Seguir un plan', 'clave')],
], rowh=[42, 58, 58, 58, 58], first_col_head=False)
done(d)

# ───────────────────────── B5 · Proyecto XP
d = Diagram('b5-02-proyecto-xp', 'Cómo funciona un proyecto XP', B5, 20, 1040, 400, 'extremeprogramming.org (mapa del proyecto) · Celina, págs. 153–156 · PF, pág. 339')
us = d.box(20, 150, 150, 60, 'Historias de usuario', weight='b', blank='clave', accept=['User Stories', 'Historias'])
sp = d.box(20, 30, 150, 60, 'Spike arquitectónico', weight='b', blank='clave', accept=['Architectural Spike', 'Spike de arquitectura'])
rp = d.box(270, 150, 170, 60, 'Planificación de entregas', weight='b', fill=HEAD, blank='clave', accept=['Release Planning', 'Juego de la planificación', 'Planificación de la entrega'])
it = d.box(520, 150, 130, 60, 'Iteración', weight='b', blank='clave', accept=['Iteration'])
ac = d.box(730, 150, 140, 60, 'Pruebas de aceptación', weight='b', blank='clave', accept=['Acceptance Tests', 'Tests de aceptación'])
sr = d.box(900, 150, 125, 60, 'Entregas pequeñas', weight='b', blank='clave', accept=['Small Releases', 'Pequeñas entregas'])
sk = d.box(300, 300, 110, 50, 'Spike', weight='b', blank='clave')
d.arrow(right(us), left(rp))
d.note(220, 160, 'requisitos', anchor='mm', size=12)
d.arrow(right(sp), (300, 150))
d.note(285, 96, 'metáfora\ndel sistema', anchor='mm', size=12)
d.arrow(right(rp), left(it))
d.note(480, 150, 'plan de\nentregas', anchor='mm', size=12)
d.arrow(right(it), left(ac))
d.note(690, 150, 'última\nversión', anchor='mm', size=12)
d.arrow(right(ac), left(sr))
d.note(962, 120, 'aprobación del cliente', anchor='mm', size=12)
d.arrow((320, 210), (320, 300))
d.note(258, 255, 'estimaciones\ninciertas', anchor='mm', size=12)
d.arrow((390, 300), (390, 210))
d.note(452, 255, 'estimaciones\nconfiables', anchor='mm', size=12)
d.arrow(bottom(us), (800, 210), head='open', via=[(95, 372), (800, 372)])
d.note(600, 358, 'escenarios de prueba', anchor='mm', size=12)
d.arrow((800, 150), (600, 150), via=[(800, 96), (600, 96)])
d.note(700, 82, 'defectos', anchor='mm', size=12)
d.arrow((610, 210), (560, 210), via=[(610, 250), (560, 250)])
d.note(585, 268, 'siguiente iteración', anchor='mm', size=12)
done(d)

# ───────────────────────── B5 · XP en listas
d = Diagram('b5-03-xp-listas', 'XP: valores, actividades básicas y diseño simple', B5, 30, 1040, 400, 'Celina, págs. 150–152 · PF, págs. 329–335 · Parcial 2024 P11 · Recuperatorio 2024 P16')
cols = [('Valores (5)', [('Simplicidad', None), ('Comunicación', None), ('Retroalimentación', ['Feedback']), ('Coraje', ['Valentía']), ('Respeto', None)]),
        ('Actividades básicas (4)', [('Programar', ['Codificar']), ('Probar', None), ('Escuchar', None), ('Diseñar', ['Diseño'])]),
        ('Un diseño es simple si… (4)', [('Ejecuta todas las pruebas', ['Pasa todas las pruebas']), ('No tiene lógica duplicada', ['Sin lógica duplicada', 'No tiene duplicación']), ('Declara las intenciones importantes', ['Declara todas las intenciones importantes de los programadores']), ('Tiene la menor cantidad de clases y métodos', ['Menor cantidad de clases y métodos'])])]
ws = [280, 280, 440]
x = 20
for (tt, items), cwid in zip(cols, ws):
    d.box(x, 20, cwid - 12, 44, tt, weight='b', fill=HEAD, r=4)
    for k, (itx, acc) in enumerate(items):
        d.box(x, 76 + k * 58, cwid - 12, 48, itx, size=15, weight='r', fill=BG, r=4, blank='clave', accept=acc)
    x += cwid
done(d)

# ───────────────────────── B6 · Costos de calidad
d = Diagram('b6-01-costos-de-calidad', 'Costo de la calidad', B6, 10, 1000, 380, 'Pressman, cap. de calidad · Copia de Apunte Diseño, págs. 235–238 · PF, págs. 352–353')
root = d.box(380, 20, 240, 50, 'Costo de la calidad', weight='b', fill=HEAD)
cs = [(60, 'Prevención', 'Planificación, capacitación, actividades técnicas tempranas. Visión proactiva.', ['Costos de prevención']),
      (380, 'Evaluación', 'Revisiones, pruebas, recolección de datos: todo lo que hace falta para medir la calidad.', ['Costos de evaluación']),
      (700, 'Fallas', 'No existirían si no hubiera errores. Es la categoría más cara.', ['Costos de fallas', 'Falla', 'Fallos'])]
for x, n, desc, acc in cs:
    b = d.box(x, 120, 240, 50, n, weight='b', blank='clave', accept=acc)
    d.arrow(bottom(root), top(b), head='none')
    d.text(x + 120, 205, desc, size=13, color=MUTED, maxw=250)
fi = d.box(580, 270, 190, 48, 'Internas', weight='b', blank='clave', accept=['Fallas internas'])
fe = d.box(790, 270, 190, 48, 'Externas', weight='b', blank='clave', accept=['Fallas externas'])
d.arrow((820, 240), top(fi), head='none')
d.arrow((820, 240), top(fe), head='none')
d.note(675, 338, 'antes de entregar', anchor='mm', size=12)
d.note(885, 338, 'después de entregar:\nlas más costosas', anchor='mm', size=12)
done(d)

print('huecos en total:', total)
