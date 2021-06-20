
#  <div align="center"> Traffic accidents in Barcelona: data analysis and modelling  </p>

*The following article and its related repository are part of the Capstone Project for the Data Science and Big Data Postgraduate Course at Universitat de Barcelona, 2020-2021.*

Authors:

* Marc Iñigo Albalate
* Leonardo Gabriel Papi
* Miguel José Santos Vaz


## Introduction 

De acuerdo a la Organización Mundial de la Salud, como consecuencia de accidentes viales cada año mueren alrededor de 1.3 millones de personas en todo el mundo. Mientras que el número de lesionados a nivel mundial varía entre 20 y 50 millones de personas.

**Principales datos:**

* Los accidentes son un riesgo muy superior para niños y jóvenes: Se trata de la primer causa de muerte en personas de entre 5 y 29 años.
* La mitad de los accidentes ocurridos, tienen consecuencias sobre peatones, ciclistas y motociclistas.
* Factores de riesgo: velocidad, conducción bajo los efectos del alcohol, no utilización de elementos de seguridad (cinturón de seguridad, casco, etc), conducción distraída e infraestructura vial insegura.
<br>
En el marco de la Union Europea, en la actualidad se producen por año alrededor de 49 muertes por millón de habitantes, frente a las 174 por millón en el mundo.
Si bien se trata del continente con menor siniestralidad en carreteras en el mundo, el obejtivo para 2030 es reducir a la mitad el número de muertes y lesiones graves. 
<br>En el año 2020, se han visto reducidos los niveles de siniestralidad en todo el continente, y según la Comisión Europea, "el menor volumen de tráfico como consecuencia de la pandemia sanitaria ha tenido un impacto directo, aunque no medible, en esta bajada de la siniestralidad vial". En el caso de España, se encuentra entre los 4 primeros países europeos con menor número de muertes (29 por millón).
<br>
Por último, la Ciudad de Barcelona ha tenido durante los últimos 10 años resultados dispares: si bien el número de muertos se ha reducido considerablemente (39 muertos en 2010 - 22 muertos en 2019), el número de accidentes registrados se ha incrementado. Las restricciones de movilidad producto de la pandemia de COVID-19 claramente han tenido un efecto en la siniestralidad, dado que durante 2020 se han reducido un 38% los siniestros en la ciudad.
En la actualidad, la ciudad cuenta con un "Plan local de seguridad vial 2019-2022", con el objetivo de reducir un 20% las victimas de accidentes.



## Project Overview

El objetivo principal del presente proyecto es el de generar un modelo de aprendizaje automático capaz de catalogar información relacionada a accidentes de tránsito. Más precisamente, buscamos que el algoritmo pueda identificar si un determinado accidente de tránsito ha ocurrido en un marco de restricciones sanitarias, como las ocurridas como consecuencia de la Pandemia de COVID-19.
Para este proyecto, hemos utilizado información de los accidentes de tránsito ocurridos en la Ciudad de Barcelona, durante los últimos 10 años. Se trata de un dataset muy completo compartido por el Ayuntamiento de Barcelona, a través del sitio web: Open Data BCN (https://opendata-ajuntament.barcelona.cat).

Dicha web, cuenta con un total de 5 diferentes dataset relacionados con accidentes de tránsito en la Ciudad. Cada dataset detalla cada uno de los accidentes ocurridos en la Ciudad (identificados con un número de expediente único) pero con información desde diferentes perspectivas. Los datasets son los siguientes:

* People involved in accidents managed by the Police in the city of Barcelona 
* Vehicles involved in accidents handled by the police in the city of Barcelona 
* Accidents managed by the local police in the city of Barcelona
* Description of the accidents' handled by the police in the city of Barcelona causality 
* Accidents managed by the Guàrdia Urbana in the city of Barcelona according to type

Para "alimentar el modelo", hemos usado el dataset nro 3 - **"Accidents managed by the local police in the city of Barcelona"**, con información desde el año 2010 a 2020. Cabe aclarar que solo el dataframe correspondiente al año 2020 contiene accidentes generados durante la pandemia de COVID-19, con lo cual nos hemos contactado con el Ayuntamiento de la Ciudad para solicitar información sobre accidentalidad durante 2021. Al día de hoy no hemos recibido dicha información.

Por otro lado, en pos de hacer un análisis más abarcativo respecto de la accidentalidad en la ciudad y sus consecuencias, hemos generado una serie de gráficos estadísticos sobre la evolución de los accidentes, víctimas, barrios con mayor cantidad de siniestros, etc. Este análisis se encuentra en el notebook 
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


sources: 

https://www.who.int/es/news-room/fact-sheets/detail/road-traffic-injuries
https://ec.europa.eu/commission/presscorner/detail/es/ip_20_1003
https://www.europarl.europa.eu/news/es/headlines/society/20190307STO30715/seguridad-vial-nuevas-medidas-europeas-para-reducir-los-accidentes-de-trafico
https://opendata-ajuntament.barcelona.cat/data/en/dataset/accidents-persones-gu-bcn
https://www.barcelona.cat/infobarcelona/es/nuevo-plan-de-seguridad-vial-para-reducir-en-un-20-a-las-victimas-de-accidentes-de-trafico_880868.html



(WORK ON PROGRESS)
