# Entradas y resultados de las actividades del PUDS

Bloque B3 de Gráficos (después de los flujos): las figuras originales del libro (las que muestran, para cada actividad, el trabajador,
los artefactos de entrada y los de resultado) con todo su texto tapado.

1. `labels.txt`: el texto de cada figura, transcripto a mano mirando la imagen (una etiqueta por línea).
2. `ocrlines.py` + `match.py`: ubica cada etiqueta en la imagen con las líneas que lee tesseract. El nombre y el estado
   entre paréntesis («(esbozado)», «(terminado)»…) quedan como huecos separados; el estado es nivel «extra».
3. `fix*.txt` (se aplican con `fix.py`): correcciones a mano de las cajas que el OCR ubicó mal, revisadas sobre la imagen.
4. `build.py`: escribe `src/graficos/b3b-*.webp/json` (las imágenes con epígrafe se recortan para que no revele la
   actividad) y actualiza la versión para completar de la figura original en `src/figuras/huecos/`.
