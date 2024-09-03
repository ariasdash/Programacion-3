from sodapy import Socrata
import pandas as pd

def Extraer(departamento, limite):

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    client = Socrata("www.datos.gov.co", None)

    results = client.get("gt2j-8ykr", where=f"departamento_nom='{departamento}'", limit=limite)

    if results:
        df = pd.DataFrame.from_records(results)
        df = df[['departamento_nom', 'ciudad_municipio_nom', 'edad', 'fuente_tipo_contagio', 'estado']] 
        return df
    else:
        print("No se encontraron datos para el departamento especificado.")
        return None

