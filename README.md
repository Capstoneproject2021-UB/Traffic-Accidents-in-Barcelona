
(WORK ON PROGRESS)


#  <div align="center"> Traffic accidents in Barcelona: data analysis and modelling  </p>

*The following article and its related repository are part of the Capstone Project for the Data Science and Big Data Postgraduate Course at Universitat de Barcelona, 2020-2021.*

Authors:

* Marc Iñigo Albalate
* Leonardo Gabriel Papi
* Miguel José Santos Vaz


## Introduction and Project Overview

El objetivo principal del presente proyecto es el de generar un modelo de aprendizaje automático capaz de catalogar informacion relacionada a accidentes de transito. Mas precisamente, buscamos que el algoritmo pueda identificar si un determinado accidente de transito ha ocurrido en un marco de restricciones sanitarias, como las ocurridas como consecuencia de la Pandemia de COVID-19.
Para este proyecto, hemos utilizado información de los accidentes de tránsito ocurridos en la Ciudad de Barcelona, durante los ultimos 10 años. Se trata de un dataset muy completo compartido por el Ayuntamiento de Barcelona, a través del sitio web: Open Data BCN (https://opendata-ajuntament.barcelona.cat).

Dicha web, cuenta con un total de 5 diferentes datasets relacionados con accidentes de tránsito en la Ciudad. Cada dataset detalla cada uno de los accidentes ocurridos en la Ciudad (identificados con un número de expediente único) pero con información desde diferentes perspectivas. Los datasets son los siguientes:

* People involved in accidents managed by the Police in the city of Barcelona 
* Vehicles involved in accidents handled by the police in the city of Barcelona 
* Accidents managed by the local police in the city of Barcelona
* Description of the accidents' handled by the police in the city of Barcelona causality 
* Accidents managed by the Guàrdia Urbana in the city of Barcelona according to type

Para "alimentar el modelo", hemos usado el dataset nro 3 - **"Accidents managed by the local police in the city of Barcelona"**, con informacion desde el año 2010 a 2020. Cabe aclarar que, dado que solo el dataframe correspondiente al año 2020 contiene accidentes generados durante la pandemia de COVID-19, por lo que nos hemos contactado con el Ayuntamiento de la Ciudad para solicitar información sobre accidentalidad durante 2021. Pero al día de hoy no hemos recibido dicha información.

Por otro lado, en pos de hacer un análisis más abarcativo respecto de la accidentalidad en la ciudad y sus consecuencias, hemos generado una serie de graficos estadísticos sobre la evolución de la accidentalidad, victimas, barrios con mayor accidentalidad, etc. Este análisis se encuentra en el notebook 
**2. Data analysis and exploration**. En este caso, hemos utilizado el dataframe mencionado anteriomente junto con el dataset: **People involved in accidents managed by the Police in the city of Barcelona**.

Este trabajo, se encuentra organizado de la siguiente forma:

* Un fichero con todos los dataframes de 2010 a 2020, correspondientes a los 2 dataset utilizados.
* Un notebook llamado *ETL*, el cual homogeneiza la información y une los dataframes en 2 únicos archivos.
* Un notebook llamado *Data analysis and exploration*. con un análisis contextual sobre la accidentalidad entre 2010 a 2020 en la Ciudad.
* Un notebook llamado *Modelos* 

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
