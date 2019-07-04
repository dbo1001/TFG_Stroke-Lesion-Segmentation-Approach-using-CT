# Aproximación hacia la identificación automática de lesión de ictus en TC craneal
### Autor: Bárbara Sainz Crespo
#### Tutores: Dr. Álvar Arnaiz González y Dr. José Francisco Díez Pastor
TFG Ingeniería Informática - Universidad de Burgos


## Introducción breve

El ictus es una enfermedad cerebrovascular que supone la primera causa de discapacidad a largo plazo y está entre las tres primeras causas de muerte. Se calcula que una de cada 6 personas sufrirá un ictus a lo largo de su vida.
La muerte de tejido cerebral que produce (se estima que mueren 2 millones de neuronas por minuto) es irreversible y, aunque el cerebro tiene cierta capacidad de regeneración y neuroplasticidad, son funciones muy limitadas.

En general, la lesión final irreversible se puede identificar con técnicas de neuroimagen a las 24h del ictus y apostamos en concreto por la tomografía computacional (TC) simple, dada su conveniencia en cuanto a disponibilidad y rapidez. Identificar el volumen y localización del tejido dañado aportará información sobre las posibles secuelas y cómo tratarlas de forma más específica y eficaz.
La disponibilidad y brevedad a la hora de atender este tipo de casos es clave, por ello trataremos de investigar cómo las aplicaciones de Ingeniería Informática podrían ayudar a identificar automáticamente las lesiones de ictus.

## Planteamiento y objetivo

Se propone explorar el papel que puede jugar la Inteligencia Artificial usando redes neuronales convolucionales (CNN) y aprendizaje profundo, para realizar una segmentación de la lesión isquémica con este tipo de técnicas de neuroimagen 3D.
En este sentido, la idea y objetivo principal de este proyecto es experimentar para tratar de aproximar la identificación
de lesión del ictus en TC craneal, mediante aprendizaje automático supervisado.

## Desarrollo

Además del trabajo propio de investigación, se siguen ciertos procedimientos en el desarrollo de este trabajo experimental, resumidos en:

 - Procesado previo de las imágenes de TC craneal (formato y etiquetado).
 
 - Entrenamiento de un modelo mediante aprendizaje supervisado, utilizando principalmente CNN volumétricas y densas (V-Net), para la segmentación de TC craneal.
 
 - Segmentación o inferencia de imágenes de TC craneal usando los pesos del modelo previamente entrenado.
 
 - Evaluación de los resultados obtenidos en la segmentación.
 
 #### Herramientas principales
 
 NiftyNet (entrenamiento, segmentación y evaluación), MRIcron (conversión de formato de TC craneal a NIfTI y su visionado), FSLview (etiquetado de TC craneal para crear la máscara con la lesión de ictus marcada)

