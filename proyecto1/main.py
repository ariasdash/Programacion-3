from API import datos as api
from UI import interfaz as ui
from tabulate import tabulate

departamento, num_casos = ui.interfaz()

df = api.Extraer(departamento, num_casos)

if df is not None:
    print(tabulate(df, headers=('NUMERO DE REGISTRO', 'CIUDAD', 'DEPARTAMENTO',  'EDAD', 'TIPO', 'ESTADO', 'PAIS DE PROCEDENCIA'), tablefmt='github', showindex=True))
else:
    print("No se encontraron datos para el departamento especificado.")