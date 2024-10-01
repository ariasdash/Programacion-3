from API import datos as api
from UI import interfaz as ui
from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
print("Columnas con datos faltantes::",df.columns[df.isnull().any()].tolist())
missing_indices = df[df.isnull().any(axis=1)].index.tolist()
print("Indices con datos faltantes:", missing_indices)
print("Estadisticas generales::")
print(df.info())
print("Resumen de estadisticas::" )
print(df.describe())
df.replace("N/A", np.nan, inplace=True)
df = df.dropna(subset=['departamento_nom', 'ciudad_municipio_nom', 'edad', 'fuente_tipo_contagio', 'estado'])
print("Datos limpios::")

fallecidos = df[df['estado'] == 'Fallecido']

plt.figure(figsize=(12, 6))
moda_fallecidos = int(fallecidos['edad'].mode()[0])
print(type(moda_fallecidos))
plt.hist(fallecidos['edad'], bins=50, color='cyan', label=f'moda {moda_fallecidos:.0f} años')
plt.legend()
plt.title(f'Distribución de Fallecimientos por Edades en el Departamento de {departamento}')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()


