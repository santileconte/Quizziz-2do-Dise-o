# Huecos sobre las figuras originales

Genera `src/figuras/huecos/<figura>.json`: los huecos para completar que tapan el texto de cada figura.
Solo se dejaron textos que se pudieron asegurar del todo.

1. `ocr.py`, `ocr2.py`, `ocr3.py`: dos lecturas independientes con tesseract (líneas con posición y texto corrido).
2. `labels.py` / `labels2.py`: arma las etiquetas (líneas que van juntas, sin cruzar bordes de cajas) y se queda con las que
   pasan todo: palabras del vocabulario de los apuntes, confianza alta y el mismo texto en la otra lectura o en otra
   versión de la figura.
3. `sheets.py`: hojas de revisión (recorte de la figura + texto leído). Cada hueco se revisó a ojo;
   `review.txt` y `review2.txt` guardan lo descartado (`X`), las figuras descartadas enteras (`XX`) y las correcciones (`=`).
4. `raw.py` + `manual.txt`: figuras de examen, de la cátedra y del libro cuyo texto se transcribió a mano mirando la figura
   (coordenadas en la imagen de revisión de 1100 px de ancho); `manual_build.py` las convierte.
5. Se escriben los JSON con un margen chico alrededor del texto. Se descartan las figuras con menos de 3 huecos seguros.
