# Repaso DSI

App para repasar el segundo parcial de Diseño de Sistemas de Información.
Es una adaptación independiente de otra app de repaso: mismo diseño, mismas secciones y mismos métodos de estudio, con contenido de DSI.

```bash
npm install
npm run dev        # abre el sitio en el navegador
npm run build      # genera dist/, que se puede abrir o subir a cualquier hosting estático
```

El progreso se guarda en el navegador (localStorage, claves `repaso-dsi:*`).

## Secciones

1. **Gráficos.** 56 gráficos para completar: los cinco flujos de trabajo del PUDS, las entradas y resultados de 23 actividades del PUDS (figuras originales del libro con el texto tapado), el ciclo de vida, las estructuras de Bass, el escenario de calidad, las tácticas, los estilos y las estructuras de los patrones GoF.
   - **Estudio**, **Práctica** (corrección al instante, segunda oportunidad, pistas) y **Simulacro** (sin ayudas, con cronómetro).
   - Filtros **Clave**, **Todo** y **Mis errores**. Un concepto queda dominado al acertarlo 2 veces seguidas.
   - **Practicar en serie:** un bloque entero o todo junto.
   - Los gráficos están **redibujados** para este repaso. Cada uno dice en qué figura, apunte y diapositiva se basa (`fuente` en su `.json`).
2. **Cuestionarios.** Por fuente, bloque, tema y formato, en modo práctica o simulacro.
   - **De la cátedra, sin retocar:** parcial y recuperatorio 2024, simulación 2024, cuestionarios semanales 2026, las preguntas del Quizziz que no están en otro registro y las figuras GoF y diagramas del PUDS del simulador.
   - **Práctica, que no es de la cátedra:** preguntas generadas con IA que venían en la carpeta y preguntas nuevas de este repaso. Cada pregunta lleva su etiqueta y su fuente.
   - Una pregunta repetida en varios registros figura una sola vez; las demás apariciones (por ejemplo, «también en el Quizziz») quedan anotadas en su fuente.
   - Selección múltiple puntúa como en las revisiones de Moodle de 2024: cada correcta suma y cada incorrecta resta.
   - Las preguntas con **clave sin verificar** se pueden responder, pero no suman puntaje ni progreso.
3. **Crucigramas.** Uno por mapa mental.
4. **Mapas mentales.** 33 mapas, uno por tema. Al tocar un concepto se abre su explicación en el apunte de estudio, con la página del apunte, de las diapositivas o del libro de donde sale.
5. **Temario.** Los temas en el orden de las clases, con prioridad, fuentes, evidencia de 2024, registros analizados y pendientes de verificación.


### Figuras originales

`#/figuras` reúne las 479 figuras de los apuntes, las diapositivas, el Word de la cátedra y los exámenes, separadas por tema (`#/figuras/23`, por ejemplo). Cada figura distinta aparece una sola vez con todas sus páginas de origen; las versiones con diferencias relevantes van por separado. Dentro de cada tema el orden es: tomadas en parciales reales, usadas por la cátedra (simulaciones, cuestionarios, práctica), mostradas en clase, apunte base y complementarias. Se abren en un visor con zoom (rueda, pellizco, doble clic o botones) y se pueden abrir en tamaño original. El proceso de extracción está en `tools/figuras/`.

#### Figuras para completar

252 de las figuras originales también se pueden completar (1425 huecos): los huecos tapan el texto de la propia figura y se
practican igual que los gráficos del inicio (Estudio, Práctica, Simulacro), una por una o en serie por tema
(`#/serie/fig-<tema>`). Solo se taparon textos que se pudieron asegurar: leídos con OCR, confirmados por una segunda lectura
o por otra versión de la figura y revisados uno por uno, o transcriptos a mano. Cómo se generan: `tools/figuras/huecos/`.

## Dónde está el contenido

| Qué | Dónde |
| --- | --- |
| Temas, prioridades y fuentes | `src/temario.ts` |
| Parcial y recuperatorio 2024 (transcripción literal) | `src/cuestionarios/parcial-2024.ts`, `recuperatorio-2024.ts` |
| Simulación 2024 y cuestionarios 2026 | `src/cuestionarios/simulacro-catedra.ts`, `cuestionarios-catedra.ts` |
| Quizziz (preguntas nuevas y mapa de repetidas) | `src/cuestionarios/quizziz.ts` |
| Figuras GoF y diagramas del PUDS | `src/cuestionarios/practica-figuras-gof.ts`, `practica-diagramas-puds.ts` |
| Práctica que no es de la cátedra | `src/cuestionarios/practica-multiple-choice.ts`, `practica-simulacro-ia.ts`, `propias.ts` |
| Figuras de las preguntas | `src/cuestionarios/img/` |
| Claves confirmadas y versiones reemplazadas | `src/cuestionarios/verificadas.ts` |
| Apunte de estudio y mapas | `tools/contenido_apunte.py`, `tools/contenido_mapas.py` → `python3 tools/build_apunte.py` |
| Gráficos | `tools/graficos.py` → `python3 tools/graficos.py` (necesita Pillow) |
| Crucigramas | `src/crucigramas/datos.ts` |

## Verificar una clave en duda

Hoy no quedan claves pendientes. Si aparece una nueva:

1. Abrí **Temario → Pendientes de verificación** y anotá el id de la pregunta.
2. Confirmá la clave contra el libro o con la cátedra. Si la propuesta estaba mal, corregí el campo `a` en el archivo de la pregunta.
3. Agregá el id en `verificadas` (`src/cuestionarios/verificadas.ts`) junto con quién y cómo la confirmó. Desde ese momento se corrige sola y esa nota aparece al corregir.

Para claves contradictorias entre registros, la jerarquía es: parcial o recuperatorio real > cuestionario oficial > simulación o compilado (dentro de una categoría, la versión más reciente). La versión que pierde va en `reemplazadas`, en el mismo archivo: su texto se conserva sin cambios, pero no se practica.

## Editar los huecos de un gráfico

Con `npm run dev`, abrí el gráfico y entrá a **Editar huecos**. Arrastrás sobre el texto, escribís la respuesta y **Guardar** escribe el `.json` en `src/graficos/`.
Una imagen nueva en `src/graficos/` aparece sola; sus huecos van en un `.json` con el mismo nombre.
