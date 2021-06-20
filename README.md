
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

En el marco de la Union Europea, en la actualidad se producen por año alrededor de 49 muertes por millón de habitantes, frente a las 174 por millón en el mundo.
Si bien se trata del continente con menor siniestralidad en carreteras en el mundo, el obejtivo para 2030 es reducir a la mitad el número de muertes y lesiones graves. 
<br>En el año 2020, se han visto reducidos los niveles de siniestralidad en todo el continente, y según la Comisión Europea, "el menor volumen de tráfico como consecuencia de la pandemia sanitaria ha tenido un impacto directo, aunque no medible, en esta bajada de la siniestralidad vial". En el caso de España, se encuentra entre los 4 primeros países europeos con menor número de muertes (29 por millón).

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

## 1) Dataset y ETL

<br>
 
### 1a) Data preprocessing 

 
 Para este proyecto hemos utilizado 2 datasets relacionados con accidentes viales, que el ayuntamiento de Barcelona publica anualmente en el portal *Open data Barcelona*. 

* **People involved in accidents managed by the Police in the city of Barcelona**: *List of people who have been involved in an accident managed by the Police in the city of Barcelona have suffered some type of injury ( slightly wounded, serious injuries or death). It includes a description of the person ( driver, passenger or pedestrian), sex, age, vehicle associated person if the cause was pedestrian*

* **Accidents managed by the local police in the city of Barcelona**: *List of accidents handled by the local police in the city of Barcelona. Incorporates the number of injuries by severity, the number of vehicles and the point of impact.*

El primero es un registro con todas las personas que formaron parte en cada uno de los accidentes registrados. Por lo que podemos tener 1,2,3 o 4 filas correspondientes al mismo accidente. Todo depende del nómero de personas involucradas. Cada dataframe cuenta con 31 campos, entre los que se encuentran: fecha, barrio, descripción de la persona, edad, descripción del vehiculo involucrado, entre otros. La clave principal es el número de expediente.
El segundo es un resumen del accidente ocurrido y sus consecuencias. Cada dataframe cuenta con 26 campos, siendo los más importantes para nuestro análisis: número de lesionados leves, graves y muertos. La clave principal es el número de expediente.

Cada dataset posee un dataframe por año, iniciando el registro en el año 2010 y finalizando en 2020. Por lo que hemos trabajado con un total de 20 archivos.

Ambos datasets se han utilizado para el análisis exploratorio, pero solo el segundo para la elaboración del modelo. 

A continuación, veremos un resumen del preposesado de datos realizado (incluyendo parte del codigo):


```python
import pandas as pd
import numpy as np
import datetime
import unicodedata

#############################################
# First data entries, visualization purposes
#############################################

print("{0} INFO: Starting ETL visualization".format(datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')))

# Read data entries
df_accidents_2010 = pd.read_csv('Dataset/people_involved/2010_ACCIDENTS_PERSONES_GU_BCN_2010.csv', delimiter=',', encoding='latin1', decimal=".")
df_accidents_2011 = pd.read_csv('Dataset/people_involved/2011_ACCIDENTS_PERSONES_GU_BCN_2011.csv', delimiter=',', encoding='latin1', decimal=".")
df_accidents_2012 = pd.read_csv('Dataset/people_involved/2012_ACCIDENTS_PERSONES_GU_BCN_2012.csv', delimiter=',', encoding='latin1', decimal=".")
df_accidents_2013 = pd.read_csv('Dataset/people_involved/2013_ACCIDENTS_PERSONES_GU_BCN_2013.csv', delimiter=',', encoding='latin1', decimal=".")
df_accidents_2014 = pd.read_csv('Dataset/people_involved/2014_ACCIDENTS_PERSONES_GU_BCN_2014.csv', delimiter=',', encoding='latin1', decimal=".")
df_accidents_2015 = pd.read_csv('Dataset/people_involved/2015_ACCIDENTS_PERSONES_GU_BCN_2015.csv', delimiter=',', encoding='latin1', decimal=".")
df_accidents_2016 = pd.read_csv('Dataset/people_involved/2016_accidents_persones_gu_bcn.csv', delimiter=',', encoding='utf8', decimal=".")
df_accidents_2017 = pd.read_csv('Dataset/people_involved/2017_accidents_persones_gu_bcn_.csv', delimiter=',', encoding='utf8', decimal=".")
df_accidents_2018 = pd.read_csv('Dataset/people_involved/2018_accidents_persones_gu_bcn_.csv', delimiter=',', encoding='utf8', decimal=".")
df_accidents_2019 = pd.read_csv('Dataset/people_involved/2019_accidents_persones_gu_bcn_.csv', delimiter=',', encoding='utf8', decimal=".")
df_accidents_2020 = pd.read_csv('Dataset/people_involved/2020_accidents_persones_gu_bcn.csv', delimiter=',', encoding='utf8', decimal=".")

# Prepare column names for homogenization
df_accidents_2010.columns = df_accidents_2010.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_')
df_accidents_2011.columns = df_accidents_2011.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_')
df_accidents_2012.columns = df_accidents_2012.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_')
df_accidents_2013.columns = df_accidents_2013.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_')
df_accidents_2014.columns = df_accidents_2014.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('£', 'u').str.replace('¢', 'o').str.replace("d'", '').str.replace('.', '').str.replace('_de_', '_')
df_accidents_2015.columns = df_accidents_2015.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_')
df_accidents_2016.columns = df_accidents_2016.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df_accidents_2017.columns = df_accidents_2017.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('__', '_')
df_accidents_2018.columns = df_accidents_2018.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('__', '_')
df_accidents_2019.columns = df_accidents_2019.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('Ă§', 'c').str.replace('ç', 'c').str.replace('ó', 'o').str.lower().str.replace('.1', '').str.replace('__', '_')
df_accidents_2020.columns = df_accidents_2020.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('Ă§', 'c').str.replace('ç', 'c').str.replace('ó', 'o').str.lower().str.replace('__', '_')

df_accidents_2010.rename(columns={'nk_any': 'any'}, inplace=True)
df_accidents_2011.rename(columns={'nk_any': 'any'}, inplace=True)
df_accidents_2012.rename(columns={'nk_any': 'any'}, inplace=True)
df_accidents_2013.rename(columns={'nk_any': 'any'}, inplace=True)
df_accidents_2014.rename(columns={'nk_any': 'any'}, inplace=True)
df_accidents_2015.rename(columns={'nk_any': 'any'}, inplace=True)
df_accidents_2019.rename(columns={'nk_any': 'any'}, inplace=True)
df_accidents_2020.rename(columns={'nk_any': 'any'}, inplace=True)

# Drop useless columns and columns not present in all the history
df_accidents_2010.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal_caption', 'nom_carrer', 'codi_carrer', 'descripcio_victimitzacio'], inplace=True)
df_accidents_2011.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal_caption', 'nom_carrer', 'codi_carrer', 'descripcio_victimitzacio'], inplace=True)
df_accidents_2012.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal_caption', 'nom_carrer', 'codi_carrer', 'descripcio_victimitzacio'], inplace=True)
df_accidents_2013.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal_caption', 'nom_carrer', 'codi_carrer', 'descripcio_victimitzacio'], inplace=True)
df_accidents_2014.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'num_postal_caption', 'nom_carrer', 'codi_carrer', 'descripcio_victimitzacio'], inplace=True)
df_accidents_2015.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'num_postal_caption', 'nom_carrer', 'codi_carrer', 'descripcio_victimitzacio'], inplace=True)
df_accidents_2016.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal', 'nom_carrer', 'codi_carrer', 'descripcio_situacio', 'descripcio_victimitzacio', 'longitud', 'latitud'], inplace=True)
df_accidents_2017.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal', 'nom_carrer', 'codi_carrer', 'descripcio_situacio', 'descripcio_victimitzacio', 'longitud', 'latitud'], inplace=True)
df_accidents_2018.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal', 'nom_carrer', 'codi_carrer', 'descripcio_situacio', 'descripcio_victimitzacio', 'longitud', 'latitud'], inplace=True)
df_accidents_2019.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal', 'codi_carrer', 'descripcio_victimitzacio', 'descripcio_lloc_atropellament_vianat', 'descripcio_motiu_desplacament_vianant', 'descripcio_motiu_desplacament_conductor', 'longitud', 'latitud'], inplace=True)
df_accidents_2020.drop(columns=['dia_setmana', 'descripcio_tipus_dia', 'descripcio_torn', 'num_postal', 'nom_carrer', 'codi_carrer', 'descripcio_victimitzacio', 'descripcio_motiu_desplacament_vianant', 'descripcio_motiu_desplacament_conductor', 'longitud', 'latitud', 'descripcio_lloc_atropellament_vianat'], inplace=True)

...
```

<br>

> Como puede verse, primero leemos las 10 entradas de datos para luego homogeneizar la informacion contenida quitando simbolos y eliminando columnas con informacion que no se encuentra en todo el conjunto de dataframes.

<br>

```python
# Concat all columns now that the format is standard
df_accidents_union_all = pd.concat([df_accidents_2010, df_accidents_2011, df_accidents_2012, df_accidents_2013, df_accidents_2014, df_accidents_2015, df_accidents_2016, df_accidents_2017, df_accidents_2018, df_accidents_2019, df_accidents_2020])

# Remove accents and special character
df_accidents_union_all['descripcio_causa_vianant'] = df_accidents_union_all['descripcio_causa_vianant'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
df_accidents_union_all['desc_tipus_vehicle_implicat'] = df_accidents_union_all['desc_tipus_vehicle_implicat'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
df_accidents_union_all['nom_barri'] = df_accidents_union_all['nom_barri'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
df_accidents_union_all['nom_districte'] = df_accidents_union_all['nom_districte'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

# Save the file
df_accidents_union_all.to_csv('./accidents_homogenized_2010to2020.csv', index=False, header=True, encoding='utf-8')

print("{0} INFO: Ending ETL visualization".format(datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')))
```
<br>

> Continuamos con la estandarización de los datos, y finalmente unimos las columnas de todos los dataframes. Generando así un único archivo csv denominado *df_accidents_union_all*

<br>

```python
# Download Covid data restrictions from API
def f_read_covid():
    try:
        # This part needs to be launch only one time, if we had more data on accidents we could update it more often
        """
        df_covid = pd.read_csv('https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest.csv')
        df_covid.drop_duplicates(keep='first', inplace=True)
        if 'ESP' in df_covid.CountryCode.unique():
            df_covid = df_covid[df_covid.CountryCode == 'ESP']
            df_covid.to_csv('./covid_feature.csv', index=False, header=True, encoding='utf-8')
        """
        # If it was already generated we can simply read the file.
        df_covid = pd.read_csv('./covid_feature.csv', delimiter=',', encoding='utf-8')
    except Exception as e:
        df_covid = None
        print("{0} ERROR: retrieving covid data: {1}".format(datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S'), e))

    # We took the columns only for the most relevant restrictions
    col = ['Date', 'C2_Workplace closing', 'C3_Cancel public events',
           'C4_Restrictions on gatherings', 'C6_Stay at home requirements',
           'C7_Restrictions on internal movement']

    df_covid = df_covid[col]

    return df_covid


# Generate the feature in a scale from 0 to 10
# being 0 before Covid was discovered and 10 the highest restriction home quarantine
def f_generate_covid_feature(p_df_covid):
    print("{0} INFO: Function generate COVID-19 features".format(datetime.datetime.now().strftime(
        '%d/%m/%Y-%H:%M:%S')))
    p_df_covid = p_df_covid.dropna().copy()
    # Generate the final value giving more strength to restrictions affecting mobility
    p_df_covid['COVID_VALUE'] = p_df_covid['C2_Workplace closing'] / 3 + p_df_covid['C3_Cancel public events'] / 6 + p_df_covid['C4_Restrictions on gatherings'] / 6 + p_df_covid['C6_Stay at home requirements'] + p_df_covid['C7_Restrictions on internal movement']
    p_df_covid['COVID'] = 0

    min_val = p_df_covid[p_df_covid.COVID_VALUE != 0].COVID_VALUE.min()
    max_val = p_df_covid.COVID_VALUE.max()
    param = (max_val - min_val) / 9
    for i in range(9):
        p_df_covid.loc[
            (p_df_covid.COVID_VALUE >= min_val + i * param) & (p_df_covid.COVID_VALUE < min_val + (i + 1) * param), 'COVID'] = i + 1
    p_df_covid.loc[p_df_covid.COVID_VALUE == max_val, 'COVID'] = 10
    p_df_covid.loc[(p_df_covid.COVID_VALUE == 0) & (p_df_covid.Date < int('20200315')), 'COVID'] = 0

    p_df_covid.drop(columns=['COVID_VALUE', 'C2_Workplace closing', 'C3_Cancel public events', 'C4_Restrictions on gatherings', 'C6_Stay at home requirements', 'C7_Restrictions on internal movement'], inplace=True)

    return p_df_covid


# Add covid feature
df_feature_covid = f_read_covid()
df_feature_covid = f_generate_covid_feature(df_feature_covid)

```
<br>

> Continuamos con la estandarización de los datos, y finalmente unimos las columnas de todos los dataframes. Generando así un único archivo csv denominado *df_accidents_union_all*

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
