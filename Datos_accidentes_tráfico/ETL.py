import pandas as pd
import numpy as np
import datetime
import unicodedata

#############################################
# First data entries, visualization purposes
#############################################

print("{0} INFO: Starting ETL visualization".format(datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')))

# Read data entries
df_accidents_2010 = pd.read_csv('2010_ACCIDENTS_PERSONES_GU_BCN_2010.csv', delimiter=',', encoding='latin1')
df_accidents_2011 = pd.read_csv('2011_ACCIDENTS_PERSONES_GU_BCN_2011.csv', delimiter=',', encoding='latin1')
df_accidents_2012 = pd.read_csv('2012_ACCIDENTS_PERSONES_GU_BCN_2012.csv', delimiter=',', encoding='latin1')
df_accidents_2013 = pd.read_csv('2013_ACCIDENTS_PERSONES_GU_BCN_2013.csv', delimiter=',', encoding='latin1')
df_accidents_2014 = pd.read_csv('2014_ACCIDENTS_PERSONES_GU_BCN_2014.csv', delimiter=',', encoding='latin1')
df_accidents_2015 = pd.read_csv('2015_ACCIDENTS_PERSONES_GU_BCN_2015.csv', delimiter=',', encoding='latin1')
df_accidents_2016 = pd.read_csv('2016_accidents_persones_gu_bcn.csv', delimiter=',', encoding='utf8')
df_accidents_2017 = pd.read_csv('2017_accidents_persones_gu_bcn_.csv', delimiter=',', encoding='utf8')
df_accidents_2018 = pd.read_csv('2018_accidents_persones_gu_bcn_.csv', delimiter=',', encoding='utf8')
df_accidents_2019 = pd.read_csv('2019_accidents_persones_gu_bcn_.csv', delimiter=',', encoding='utf8')
df_accidents_2020 = pd.read_csv('2020_accidents_persones_gu_bcn.csv', delimiter=',', encoding='utf8')

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

# Sort columns alphabetically to match later on
df_accidents_2010.sort_index(axis=1, inplace=True)
df_accidents_2011.sort_index(axis=1, inplace=True)
df_accidents_2012.sort_index(axis=1, inplace=True)
df_accidents_2013.sort_index(axis=1, inplace=True)
df_accidents_2014.sort_index(axis=1, inplace=True)
df_accidents_2015.sort_index(axis=1, inplace=True)
df_accidents_2016.sort_index(axis=1, inplace=True)
df_accidents_2017.sort_index(axis=1, inplace=True)
df_accidents_2018.sort_index(axis=1, inplace=True)
df_accidents_2019.sort_index(axis=1, inplace=True)
df_accidents_2020.sort_index(axis=1, inplace=True)

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


# Download Covid data restrictions from API
def f_read_covid():
    try:
        """
        df_covid = pd.read_csv('https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest.csv')
        df_covid.drop_duplicates(keep='first', inplace=True)
        if 'ESP' in df_covid.CountryCode.unique():
            df_covid = df_covid[df_covid.CountryCode == 'ESP']
            df_covid.to_csv('./covid_feature.csv', index=False, header=True, encoding='utf-8')
        """
        df_covid = pd.read_csv('./covid_feature.csv', delimiter=',', encoding='utf-8')
    except Exception as e:
        df_covid = None
        print("{0} ERROR: retrieving covid data: {1}".format(datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S'), e))

    col = ['Date', 'C2_Workplace closing', 'C3_Cancel public events',
           'C4_Restrictions on gatherings', 'C6_Stay at home requirements',
           'C7_Restrictions on internal movement']

    df_covid = df_covid[col]

    return df_covid


# Generate the feature in a scale from 0 to 10 being 0 before Covid was discovered and 10 home quarantine
def f_generate_covid_feature(p_df_covid):
    print("***************************************************")
    print("{0} INFO: Function generate COVID-19 features".format(datetime.datetime.now().strftime(
        '%d/%m/%Y-%H:%M:%S')))
    p_df_covid = p_df_covid.dropna().copy()
    # Generate the mean between restrictions on gatherings and on internal movements
    p_df_covid['D4'] = (p_df_covid['C4_Restrictions on gatherings'] + p_df_covid[
        'C7_Restrictions on internal movement']) / 2
    # Generate the final value
    p_df_covid['COVID_VALUE'] = p_df_covid['C2_Workplace closing'] / 6 + p_df_covid['C3_Cancel public events'] / 6 + p_df_covid['C6_Stay at home requirements'] / 2 + p_df_covid['D4'] / 6
    p_df_covid['COVID'] = 0

    min_val = p_df_covid[p_df_covid.COVID_VALUE != 0].COVID_VALUE.min()
    max_val = p_df_covid.COVID_VALUE.max()
    param = (max_val - min_val) / 9
    for i in range(9):
        p_df_covid.loc[
            (p_df_covid.COVID_VALUE >= min_val + i * param) & (p_df_covid.COVID_VALUE < min_val + (i + 1) * param), 'COVID'] = i + 1
    p_df_covid.loc[p_df_covid.COVID_VALUE == max_val, 'COVID'] = 10
    p_df_covid.loc[(p_df_covid.COVID_VALUE == 0) & (p_df_covid.Date < int('20200315')), 'COVID'] = 0

    p_df_covid.drop(columns=['COVID_VALUE', 'D4', 'C2_Workplace closing', 'C3_Cancel public events', 'C4_Restrictions on gatherings', 'C6_Stay at home requirements', 'C7_Restrictions on internal movement'], inplace=True)

    return p_df_covid


# Add covid feature
df_feature_covid = f_read_covid()
df_feature_covid = f_generate_covid_feature(df_feature_covid)

# Merge section
df_accidents_union_all['Full_Date'] = df_accidents_union_all['any'].map(str) + df_accidents_union_all['mes_any'].map(str).str.zfill(2) + df_accidents_union_all['dia_mes'].map(str).str.zfill(2)
df_accidents_union_all['Full_Date'] = df_accidents_union_all['Full_Date'].astype(int)
df_accidents_union_all = pd.merge(df_accidents_union_all, df_feature_covid, left_on="Full_Date", right_on="Date", how="left", sort=False)
df_accidents_union_all['COVID'] = df_accidents_union_all['COVID'].fillna(0)
df_accidents_union_all.drop(columns=['Date', 'dia_mes', 'mes_any'], inplace=True)

print(1)

#############################################
# Second data entries, predictions purposes
#############################################


print("{0} INFO: Starting ETL predictions".format(datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')))

# Read data entries
df_localpolice_2010 = pd.read_csv('2010_ACCIDENTS_GU_BCN_2010.csv', delimiter=',', encoding='latin1')
df_localpolice_2011 = pd.read_csv('2011_ACCIDENTS_GU_BCN_2011.csv', delimiter=',', encoding='latin1')
df_localpolice_2012 = pd.read_csv('2012_ACCIDENTS_GU_BCN_2012.csv', delimiter=',', encoding='latin1')
df_localpolice_2013 = pd.read_csv('2013_ACCIDENTS_GU_BCN_2013.csv', delimiter=',', encoding='latin1')
df_localpolice_2014 = pd.read_csv('2014_ACCIDENTS_GU_BCN_2014.csv', delimiter=',', encoding='latin1')
df_localpolice_2015 = pd.read_csv('2015_accidents_gu_bcn.csv', delimiter=';', encoding='latin1')
df_localpolice_2016 = pd.read_csv('2016_accidents_gu_bcn.csv', delimiter=',', encoding='utf8')
df_localpolice_2017 = pd.read_csv('2017_accidents_gu_bcn.csv', delimiter=',', encoding='utf8')
df_localpolice_2018 = pd.read_csv('2018_accidents_gu_bcn.csv', delimiter=',', encoding='utf8')
df_localpolice_2019 = pd.read_csv('2019_accidents_gu_bcn.csv', delimiter=',', encoding='utf8')
df_localpolice_2020 = pd.read_csv('2020_accidents_gu_bcn.csv', delimiter=',', encoding='utf8')

# Prepare column names for homogenization
df_localpolice_2010.columns = df_localpolice_2010.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2011.columns = df_localpolice_2011.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2012.columns = df_localpolice_2012.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2013.columns = df_localpolice_2013.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2014.columns = df_localpolice_2014.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('£', 'u').str.replace('¢', 'o').str.replace("d'", '').str.replace('.', '').str.replace('_de_', '_').str.replace('ú', 'u').str.replace('ó', 'o').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2015.columns = df_localpolice_2015.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace("d'", '').str.replace('ó', 'o').str.replace('.', '').str.replace('_de_', '_').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2016.columns = df_localpolice_2016.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('ú', 'u').str.replace('ó', 'o').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2017.columns = df_localpolice_2017.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('__', '_').str.replace('ú', 'u').str.replace('ó', 'o').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2018.columns = df_localpolice_2018.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('__', '_').str.replace('ú', 'u').str.replace('ó', 'o').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2019.columns = df_localpolice_2019.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('Ă§', 'c').str.replace('ç', 'c').str.replace('ó', 'o').str.lower().str.replace('.1', '').str.replace('__', '_').str.replace('ú', 'u').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')
df_localpolice_2020.columns = df_localpolice_2020.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('Ă§', 'c').str.replace('ç', 'c').str.replace('ó', 'o').str.lower().str.replace('__', '_').str.replace('ú', 'u').str.replace('_caption', '').str.replace('_d_', '_').str.replace('í', 'i').str.replace('nk_barri', 'codi_barri')

df_localpolice_2015['dia_setmana'] = df_localpolice_2015['dia_setmana'].str.replace('Dl', '1').str.replace('Dm', '2').str.replace('Dc', '3').str.replace('Dj', '4').str.replace('Dv', '5').str.replace('Ds', '6').str.replace('Dg', '7')
df_localpolice_2016['dia_setmana'] = df_localpolice_2016['dia_setmana'].str.replace('Dl', '1').str.replace('Dm', '2').str.replace('Dc', '3').str.replace('Dj', '4').str.replace('Dv', '5').str.replace('Ds', '6').str.replace('Dg', '7')
df_localpolice_2017['dia_setmana'] = df_localpolice_2017['dia_setmana'].str.replace('Dl', '1').str.replace('Dm', '2').str.replace('Dc', '3').str.replace('Dj', '4').str.replace('Dv', '5').str.replace('Ds', '6').str.replace('Dg', '7')
df_localpolice_2018['dia_setmana'] = df_localpolice_2018['dia_setmana'].str.replace('Dl', '1').str.replace('Dm', '2').str.replace('Dc', '3').str.replace('Dj', '4').str.replace('Dv', '5').str.replace('Ds', '6').str.replace('Dg', '7')
df_localpolice_2019['dia_setmana'] = df_localpolice_2019['dia_setmana'].str.replace('Dl', '1').str.replace('Dm', '2').str.replace('Dc', '3').str.replace('Dj', '4').str.replace('Dv', '5').str.replace('Ds', '6').str.replace('Dg', '7')


df_localpolice_2010.rename(columns={'nk_any': 'any'}, inplace=True)
df_localpolice_2011.rename(columns={'nk_any': 'any'}, inplace=True)
df_localpolice_2012.rename(columns={'nk_any': 'any'}, inplace=True)
df_localpolice_2013.rename(columns={'nk_any': 'any'}, inplace=True)
df_localpolice_2014.rename(columns={'nk_any': 'any'}, inplace=True)
df_localpolice_2015.rename(columns={'nk_any': 'any'}, inplace=True)
df_localpolice_2019.rename(columns={'nk_any': 'any'}, inplace=True)
df_localpolice_2020.rename(columns={'nk_any': 'any'}, inplace=True)


# Drop useless columns and columns not present in all the history
df_localpolice_2010.drop(columns=["num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2011.drop(columns=["num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2012.drop(columns=["num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2013.drop(columns=["num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2014.drop(columns=["num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2015.drop(columns=["num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2016.drop(columns=['latitud', 'longitud', "num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2017.drop(columns=['latitud', 'longitud', "num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2018.drop(columns=['latitud', 'longitud', "num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2019.drop(columns=['latitud', 'longitud', "num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)
df_localpolice_2020.drop(columns=['latitud', 'longitud', "num_postal", "descripcio_dia_setmana", "descripcio_tipus_dia", "descripcio_torn", "nom_mes"], inplace=True)


# Sort columns alphabetically to match later on
df_localpolice_2010.sort_index(axis=1, inplace=True)
df_localpolice_2011.sort_index(axis=1, inplace=True)
df_localpolice_2012.sort_index(axis=1, inplace=True)
df_localpolice_2013.sort_index(axis=1, inplace=True)
df_localpolice_2014.sort_index(axis=1, inplace=True)
df_localpolice_2015.sort_index(axis=1, inplace=True)
df_localpolice_2016.sort_index(axis=1, inplace=True)
df_localpolice_2017.sort_index(axis=1, inplace=True)
df_localpolice_2018.sort_index(axis=1, inplace=True)
df_localpolice_2019.sort_index(axis=1, inplace=True)
df_localpolice_2020.sort_index(axis=1, inplace=True)

# Concat all columns now that the format is standard
df_localpolice_union_all = pd.concat([df_localpolice_2010, df_localpolice_2011, df_localpolice_2012, df_localpolice_2013, df_localpolice_2014, df_localpolice_2015, df_localpolice_2016, df_localpolice_2017, df_localpolice_2018, df_localpolice_2019, df_localpolice_2020])


# Remove accents and special character
df_localpolice_union_all['descripcio_causa_vianant'] = df_localpolice_union_all['descripcio_causa_vianant'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
df_localpolice_union_all['nom_barri'] = df_localpolice_union_all['nom_barri'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
df_localpolice_union_all['nom_districte'] = df_localpolice_union_all['nom_districte'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

# merge any
df_localpolice_union_all['any'] = df_localpolice_union_all['any'].astype(str)
df_localpolice_union_all['mes_any'] = df_localpolice_union_all['mes_any'].astype(int)
df_localpolice_union_all['dia_mes'] = df_localpolice_union_all['dia_mes'].astype(int)
df_localpolice_union_all['Full_Date'] = df_localpolice_union_all['any'].map(str) + df_localpolice_union_all['mes_any'].map(str).str.zfill(2) + df_localpolice_union_all['dia_mes'].map(str).str.zfill(2)
df_localpolice_union_all['Full_Date'] = df_localpolice_union_all['Full_Date'].astype(int)

# Merge section
df_localpolice_union_all['Full_Date'] = df_localpolice_union_all['any'].map(str) + df_localpolice_union_all['mes_any'].map(str).str.zfill(2) + df_localpolice_union_all['dia_mes'].map(str).str.zfill(2)
df_localpolice_union_all['Full_Date'] = df_localpolice_union_all['Full_Date'].astype(int)
df_localpolice_union_all = pd.merge(df_localpolice_union_all, df_feature_covid, left_on="Full_Date", right_on="Date", how="left", sort=False)
df_localpolice_union_all['COVID'] = df_localpolice_union_all['COVID'].fillna(0)

df_localpolice_union_all.drop(columns=['Date'], inplace=True)


# Save the file
df_localpolice_union_all.to_csv('./accidents_localpolice_homogenized_2010to2020.csv', index=False, header=True, encoding='utf-8')

print("{0} INFO: Ending ETL predictions".format(datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')))
