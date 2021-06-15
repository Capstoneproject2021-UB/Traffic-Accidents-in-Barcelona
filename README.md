
#  <div align="center"> Traffic accidents in Barcelona: data analysis and modelling  </p>

*The following article and its related repository are part of the Capstone Project for the Data Science and Big Data Postgraduate Course at Universitat de Barcelona, 2020-2021.*

Authors:

* Marc Iñigo Albalate
* Leonardo Gabriel Papi
* Miguel José Santos Vaz


## Introduction and Project Overview

El objetivo principal del presente proyecto es el de generar un modelo de aprendizaje automático capaz de catalogar información relacionada a accidentes de tránsito. Más precisamente, buscamos que el algoritmo pueda identificar si un determinado accidente de tránsito ha ocurrido en un marco de restricciones sanitarias, como las ocurridas como consecuencia de la Pandemia de COVID-19.
Para este proyecto, hemos utilizado información de los accidentes de tránsito ocurridos en la Ciudad de Barcelona, durante los últimos 10 años. Se trata de un dataset muy completo compartido por el Ayuntamiento de Barcelona, a través del sitio web: Open Data BCN (https://opendata-ajuntament.barcelona.cat).

Dicha web, cuenta con un total de 5 diferentes dataset relacionados con accidentes de tránsito en la Ciudad. Cada dataset detalla cada uno de los accidentes ocurridos en la Ciudad (identificados con un número de expediente único) pero con información desde diferentes perspectivas. Los datasets son los siguientes:

* People involved in accidents managed by the Police in the city of Barcelona 
* Vehicles involved in accidents handled by the police in the city of Barcelona 
* Accidents managed by the local police in the city of Barcelona
* Description of the accidents' handled by the police in the city of Barcelona causality 
* Accidents managed by the Guàrdia Urbana in the city of Barcelona according to type

Para "alimentar el modelo", hemos usado el dataset nro 3 - **"Accidents managed by the local police in the city of Barcelona"**, con información desde el año 2010 a 2020. Cabe aclarar que solo el dataframe correspondiente al año 2020 contiene accidentes generados durante la pandemia de COVID-19, con lo cual nos hemos contactado con el Ayuntamiento de la Ciudad para solicitar información sobre accidentalidad durante 2021. Al día de hoy no hemos recibido dicha información.

Por otro lado, en pos de hacer un análisis más abarcativo respecto de la accidentalidad en la ciudad y sus consecuencias, hemos generado una serie de gráficos estadísticos sobre la evolución de la accidentalidad, víctimas, barrios con mayor accidentalidad, etc. Este análisis se encuentra en el notebook 
**2. Data analysis and exploration**. En este caso, hemos utilizado el dataframe mencionado anteriormente junto con el dataset: **People involved in accidents managed by the Police in the city of Barcelona**.

Este trabajo, se encuentra organizado de la siguiente forma:

* Un fichero con todos los dataframes de 2010 a 2020, correspondientes a los 2 dataset utilizados.
* Un notebook llamado *ETL*, el cual homogeneiza la información y une los dataframes en 2 únicos archivos. Además, incorpora en dichos dataframes la "feature COVID": un valor entre rango 0 y 10. Donde 0 representa una situación previa a la existencia de la enfermedad, y 10 la mayor restricción a la movilidad ocurrida en España durante la pandemia (finales de Marzo 2020 - comienzos de Abril)
* Un notebook llamado *Data analysis and exploration*. Con un análisis contextual sobre la accidentalidad entre 2010 a 2020 en la Ciudad.
* Un notebook con el nombre de *Modelos*. En el mismo, se utiliza una librería de auto Machine-Learning TPOT (http://epistasislab.github.io/tpot/) para seleccionar el modelo más adecuado al problema que estamos abordando.
Ante la falta de datos de accidentalidad durante 2021, el modelo fue modificado para generar predicciones a un nivel de agregación por distrito y por mes. En caso que obtengamos dicha información en los siguientes días, modificaremos el modelo acorde a nuestro objetivo inicial: identificar aquellos accidentes en situación de restricción de la movilidad.




(TRABAJO EN PROCESO) 
(TRABAJO EN PROCESO) 

## Dataset
  a)
  b) data preprocessing 

## Analysis
 a) Data Exploration
 b) Exploratory Visualization
 c) Relationship between the features

## Modelization

## Conclusion

## References


source: https://opendata-ajuntament.barcelona.cat/data/en/dataset/accidents-persones-gu-bcn


(WORK ON PROGRESS)
