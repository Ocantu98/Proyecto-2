# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
#Se abre el archivo con la libreria pandaspara crear el dataframe"
df = pd.read_csv(r'C:\Users\dev1\Desktop\synergy_logistics_database.csv')
#Se imprime el data set para darnos una idea de como se ve
print(df.head())
print(df.dtypes)
print(df.describe())
#En busca de falta de valores en el dataframe
print(df.isna().any())
#Se cuenta cuantas exportaciones e importaciones se tienen por pais
print(df.groupby(['origin','direction'])['direction'].count())
#Imprimimos unas graficas de barras para observar como estan los paises de acuerdo a importaciones y exportaciones
cantidad=df.groupby(['origin','direction'])['direction'].count().unstack(level=1).plot(kind='bar',title='Cantidad de Importaciones y Exportaciones')
direction=df.groupby(['origin','direction'])['total_value'].sum().unstack(level=1).plot(kind='bar',title='Valor total de Importaciones y Exportaciones')
direction.set_ylabel("Miles de Millones")
imports=df[df['direction']=='Imports']
exports=df[df['direction']=='Exports']
#Graficas de boxplot e instogramas para ver la posible distribucion y como se comportan los datos
df.groupby(['origin'])['total_value'].sum().nlargest(10,keep='all')
imports.boxplot(column='total_value',by='origin',rot=90)
exports.boxplot(column='total_value',by='origin',rot=90)
imports.hist(column='total_value',by='origin',rot=90)
exports.hist(column='total_value',by='origin',rot=90)
#Se cuenta cuantas exportaciones e importaciones se tienen por pais
print(df.groupby(['transport_mode'])['transport_mode'].count())
print(df.groupby(['transport_mode'])['total_value'].sum())
df.groupby(['transport_mode'])['total_value'].sum().plot(kind='bar')
df.groupby(['transport_mode'])['transport_mode'].count().plot(kind='bar')
df.groupby(['origin','transport_mode'])['transport_mode'].count().unstack(level=1).plot(kind='bar',title='Cantidad de Transporte por pais')
