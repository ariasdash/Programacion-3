from API import datos as api
from UI import interfaz as ui
from tabulate import tabulate
import pandas as pd
import numpy as np

departamento, num_casos = ui.interfaz()

df = api.Extraer(departamento, num_casos)

if df is not None:
    print(tabulate(df, headers=('NUMERO DE REGISTRO', 'CIUDAD', 'DEPARTAMENTO',  'EDAD', 'TIPO', 'ESTADO', 'PAIS DE PROCEDENCIA'), tablefmt='github', showindex=True))
else:
    print("No se encontraron datos para el departamento especificado.")
    
    exit()

print("Filas:", df.shape[0])
print("Columndas:", df.shape[1])
print("Nombre columnas:", df.columns.values.tolist())
print("Yipo de datos columnas:\n", df.dtypes)
df.replace("N/A", np.nan, inplace=True)
print("Columnas con datos faltantes::",df.columns[df.isnull().any()].tolist())
missing_indices = df[df.isnull().any(axis=1)].index.tolist()
print("Indices con datos faltantes:", missing_indices)
print("Estadisticas generales::")
print(df.info())
print("Resumen de estadisticas::" )
print(df.describe())
df = df.dropna(subset=['departamento_nom', 'ciudad_municipio_nom', 'edad', 'fuente_tipo_contagio', 'estado'])
print("Datos limpios::")
print(tabulate(df, headers=('NUMERO DE REGISTRO', 'CIUDAD', 'DEPARTAMENTO',  'EDAD', 'TIPO', 'ESTADO', 'PAIS DE PROCEDENCIA'), tablefmt='github', showindex=True))
