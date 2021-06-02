import pandas as pd
import numpy as np
import datetime
import unicodedata


df_localpolice_union_all = pd.read_csv('accidents_localpolice_homogenized_2010to2020.csv', delimiter=',', encoding='utf8')

#############################################
# AUTO ML - TPOT
#############################################

# conda install -c conda-forge tpot
from tpot import TPOTRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

df_localpolice_union_all.drop(columns=['hora_dia', 'codi_barri', 'codi_carrer', 'codi_districte', 'coordenada_utm_x', 'coordenada_utm_y', 'descripcio_causa_vianant', 'nom_barri', 'nom_carrer', 'numero_expedient', 'Full_Date'], inplace=True)
df_localpolice_union_all.drop(columns=['dia_setmana', 'numero_lesionats_greus', 'numero_lesionats_lleus', 'numero_vehicles_implicats'], inplace=True)
# df_localpolice_union_all.drop(columns=['numero_vehicles_implicats','numero_victimes'], inplace=True)

# Group by to make predictions by district and month
df_localpolice_union_all.drop(columns=['COVID'], inplace=True)
df_localpolice_union_all = df_localpolice_union_all.groupby(['nom_districte', 'any', 'mes_any']).agg({'numero_victimes': 'sum'}).reset_index()
#df_localpolice_union_all = df_localpolice_union_all.groupby(['nom_districte', 'any', 'mes_any']).agg({'numero_victimes': 'sum', 'COVID': 'mean'}).reset_index()

# ONE HOT ENCODING
# one_hot_encoding = pd.get_dummies(df_localpolice_union_all.dia_setmana, prefix='dia_setmana')
# df_localpolice_union_all = pd.concat([df_localpolice_union_all, one_hot_encoding], axis=1)
one_hot_encoding = pd.get_dummies(df_localpolice_union_all.mes_any, prefix='mes_any')
df_localpolice_union_all = pd.concat([df_localpolice_union_all, one_hot_encoding], axis=1)
one_hot_encoding = pd.get_dummies(df_localpolice_union_all.nom_districte, prefix='nom_districte')
df_localpolice_union_all = pd.concat([df_localpolice_union_all, one_hot_encoding], axis=1)
df_localpolice_union_all.drop(columns=['mes_any', 'nom_districte'], inplace=True)

# GROUP BY DISTRICT

# Split train dataset
variable_objetivo = 'numero_victimes'
df_train_x = df_localpolice_union_all[df_localpolice_union_all['any'] < 2020].copy()
df_train_x = df_train_x.append(df_localpolice_union_all.query('any == 2020 & mes_any_9 != 1 & mes_any_10 != 1 & mes_any_11 != 1 & mes_any_12 != 1'), ignore_index = True)


# df_train_x["any"] = pd.to_numeric(df_train_x["any"])
# df_localpolice_union_all["COVID"] = df_localpolice_union_all["COVID"].astype(np.int64)
# df_train_x = df_train_x.apply(pd.to_numeric)
df_train_x = df_train_x.fillna(0)
df_train_y = df_train_x[variable_objetivo]
df_train_x.drop(columns=[variable_objetivo], inplace=True)

df_train_x = df_train_x.to_numpy()
df_train_y = df_train_y.to_numpy()

# df_test_x = df_localpolice_union_all[df_localpolice_union_all['any'] == 2020 & df_localpolice_union_all['mes_any'] > 11].copy()
df_test_x = df_localpolice_union_all.query('(any == 2020 & mes_any_9 == 1) | (any == 2020 & mes_any_10 == 1) | (any == 2020 & mes_any_11 == 1) | (any == 2020 & mes_any_12 == 1)')

# df_test_x = df_test_x.apply(pd.to_numeric)
df_test_x = df_test_x.fillna(0)
df_test_y = df_test_x[variable_objetivo]
df_test_x.drop(columns=[variable_objetivo], inplace=True)

df_test_x = df_test_x.to_numpy()
df_test_y = df_test_y.to_numpy()

df_train_x = np.where(np.isnan(df_train_x), 0, df_train_x)
df_train_y = np.where(np.isnan(df_train_y), 0, df_train_y)
df_test_x = np.where(np.isnan(df_test_x), 0, df_test_x)
df_test_y = np.where(np.isnan(df_test_y), 0, df_test_y)

print(df_train_x.shape)
print(type(df_train_x))
print(df_train_y.shape)
print(type(df_train_y))
print(df_test_x.shape)
print(type(df_test_x))
print(df_test_y.shape)
print(type(df_test_y))

# Un-coment here to train the model

tpot = TPOTRegressor(generations=25, population_size=50, verbosity=2, random_state=0, n_jobs=-1, scoring='r2')
# tpot = TPOTRegressor(generations=5, population_size=10, early_stop=1, cv=tscv, random_state=0, verbosity=2, scoring='r2', n_jobs=-1)
tpot.fit(df_train_x, df_train_y)
# Clean the result-text to get only the header, imports and parameters with the best model, which will be ran
with open('tpot_pipeline.py', "r") as f:
    lines = f.readlines()
with open('tpot_pipeline.py', "w") as f:
    line_to_keep = False
    for line in lines:
        if line_to_keep is True:
            if line.strip("\n") != ")":
                f.write(line)
            else:
                f.write(line)
                break
                # If there is no further line, the end of the text is reached, exit
        elif ("import" in line) | ("from" in line):
            f.write(line)
        elif "exported_pipeline" in line.strip("\n"):
            line_to_keep = True
            f.write(line)
            if ")" == line.strip("\n")[-1:]:
                break
tpot.export('tpot_pipeline.py')

model = tpot
#from tpot_pipeline import exported_pipeline
#model = exported_pipeline.fit(df_train_x, df_train_y)



# import tpot_pipeline
# tpot = tpot_pipeline
# print(tpot.score(df_test_x, df_test_y))
print(model.score(df_test_x, df_test_y))
predictions = model.predict(df_test_x)
predictions[predictions < 0] = 0
predictions = np.rint(predictions)
print(predictions)
print(df_test_y)

def f_calculate_fa(y_true, y_pred):
    y_pred = np.where(y_pred > 0, y_pred, 0)
    # entry to entry calculations
    fa = np.zeros(len(y_true))
    for i in range(len(y_true)):
        bias = abs(y_true[i] - y_pred[i])
        if (y_true[i] == 0) & (y_pred[i] == 0):
            er = 0
        elif y_pred[i] == 0:
            er = bias / (1 + abs(y_true[i]))
        else:
            er = bias / y_pred[i]
        fa[i] = 1 - er
    # In order to not take into account forecasts accuracies equal to 0
    fa = fa[~np.isnan(fa)]
    fa[fa < 0] = 0
    return fa


FA = f_calculate_fa(df_test_y, predictions)
print(FA)
print(np.average(FA))
print(np.mean(FA))

"""
input_data = test_holdout.iloc[num_day]
input_data = input_data.drop(labels=['DT_DAY', 'F_VOLUME'])
input_data = input_data.values
input_data = input_data.reshape(1, input_data.shape[0])
"""
#0.9938673864414126

#############################################
# AUTO ML - MLJAR
#############################################
