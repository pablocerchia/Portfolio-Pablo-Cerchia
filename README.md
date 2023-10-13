# Portfolio-Pablo-Cerchia
Hola! Este es mi portfolio con todos los proyectos que hice hasta la fecha. En estos proyectos el lenguaje utilizado fue python y también hice uso de las librerías pandas, numpy, geopandas, spark, scikit-learn, folium y matplotlib. 

El proyecto más importante es uno que sigue construyéndose día a día. Es una página hecha con python en el framework Streamlit sobre las elecciones de 2023 en Argentina. Actualmente en la página se puede hacer lo siguiente:

- Consultar resultados en cada distrito y sección electoral. (Graficado con Flourish y Datawrapper)
- Comparación del rendimiento de las principales agrupaciones por provincia/sección electoral y también en Buenos Aires, CABA y el conurbano. (Graficado con Flourish)
- Comparación mano a mano de cómo le fue a cada candidato y agrupación en cada provincia y sección. También válido para internas de las PASO. (Graficado con Flourish)
- Las propuestas de cada candidato divididas por eje temático. Lo que dijeron en ambos debates presidenciales. Consultá su CV y accedé a la plataforma electoral de cada uno.
- Cómo quedaría la Cámara de Diputados y Senadores. Qué miembros la componen y quienes terminan su mandato en 2023. (Graficado con Flourish, tablas hechas con AGGrid, gráficos de barras hechas con Plotly)
- Calculadora D´Hondt: calculá cuántas bancas ganaría tu partido en las elecciones generales.
- Distribución de género y edad en las listas de las agrupaciones. Cuál género encabeza más las listas de cada agrupación. (Graficado con Plotly)
- Preguntas frecuentes sobre las elecciones 
- Distribución de género y edad de los electores en cada distrito del país (Graficado con Flourish y Plotly)
- Consultar resultados por mesa. Se hacen querys a un .csv, ahora estoy armando para que se pueda hacer querys directo a una base de datos y se pueda consultar los resultados de cada elección desde 2011 en todos los niveles de desagregación (nacional, provincia, sección, circuito, mesa). 

El primer proyecto consistió en realizar una calculadora de la fórmula D'Hondt.

El segundo proyecto ("Análisis JxC por Circuitos Electorales") consiste en visualizar la relación entre la variable del censo "Sexo" y el porcentaje de votos de Juntos por el Cambio. El objetivo de este proyecto fue cruzar los datos electorales con el Censo 2010 y sus respectivas geometrías y además interpretar politológicamente los resultados a nivel circuito electoral. Aquí se visualizan y analizan geográficamente datos electorales y censales. En este proyecto queda en evidencia a su vez la evolución en la eficiencia del código respecto al segundo proyecto. Si se descarga el archivo html se puede interactuar con las visualizaciones. 

En la carpeta "Modelo Machine Learning Spotify" se ubica un proyecto en el cual el objetivo fue predecir de la mejor manera posible el género de las canciones. Para eso hice primero un modelo baseline y luego mediante RandomForest y XGBoost y el tuning de hiperparámetros traté de buscar el mejor modelo posible. Para esto tuve que splitear datasets, hacer feature engineering (en donde realicé imputación de nulos, One Hot Encoding, Mean Encoding, vectorizé valores con TF-IDF y normalicé valores con la librería scikit-learn), buscar/tunear hiperparametros mediante Randomized Search y buscar las features más importantes del dataset. También hice 6 visualizaciones que ayudan a explicar o entender el target.

Luego se encuentran en las carpetas "TP Spark" y "TP Pandas" dos trabajos prácticos que hice en la materia "Organización de Datos" de la carrera de Ingeniería Informática de la UBA en donde se encuentran ejercicios y visualizaciones realizadas con esas librerías para trabajos prácticos de dicha materia. 


