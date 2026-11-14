# Cómo se armaron las figuras originales

Scripts usados para generar `src/figuras/` (imágenes y `figuras.json`). Están escritos para la carpeta de trabajo
en la que se corrieron (rutas absolutas); quedan como registro del proceso.

1. `01_candidatas.py`: extrae todas las imágenes incrustadas de los cinco PDF (`pdfimages -p`) y descarta íconos,
   viñetas y tiras de texto por tamaño y proporción. También se buscaron figuras vectoriales: solo había tablas.
2. Las 995 imágenes distintas se revisaron una por una en hojas de miniaturas. `keep.txt` lista las que son
   diagramas, esquemas o figuras (se descartaron fotos de texto, portadas, decoración y temas del primer parcial).
3. `assign.py`: asigna cada figura a un tema por el rango de páginas del temario, con correcciones manuales.
4. `apply.py`: agrupa las figuras idénticas (hash perceptual dentro de cada tema) y aplica las uniones y los cambios
   de tema revisados a mano (`fixes.txt`). Las versiones con diferencias relevantes quedan separadas.
5. `captions.py` y `titles.py`: buscan el epígrafe («Figura 7.10. …»), el título de la diapositiva o el subtítulo
   cercano para nombrar cada figura. Si no hay uno confiable, la figura queda sin título.
6. `manifest.py`: elige la mejor versión de cada figura, la guarda en WebP (sin pérdida para escaneos y diagramas,
   calidad 90 para fotos de diapositivas), genera las miniaturas y escribe `figuras.json` con el orden por prioridad.
