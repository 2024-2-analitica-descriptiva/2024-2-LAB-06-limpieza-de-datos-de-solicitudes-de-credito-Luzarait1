"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    data = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';', index_col=0)
    data.dropna(inplace=True)

    data['sexo'] = data['sexo'].str.lower()

    data['tipo_de_emprendimiento'] = data['tipo_de_emprendimiento'].str.lower().str.strip()

    data['barrio'] = data['barrio'].str.lower()
    data['barrio'] = data['barrio'].str.replace("_", " ").str.replace("-", " ")

    data['idea_negocio'] = data['idea_negocio'].str.lower()
    data['idea_negocio'] = data['idea_negocio'].str.replace("_", " ").str.replace("-", " ")
    data['idea_negocio'] = data['idea_negocio'].str.strip()

    data['monto_del_credito'] = data['monto_del_credito'].str.strip()
    data['monto_del_credito'] = data['monto_del_credito'].str.replace("$","").str.replace(",","").str.replace(".00","")
    data['monto_del_credito'] = data['monto_del_credito'].astype(int)

    data['línea_credito'] = data['línea_credito'].str.replace("_", " ").str.replace("-", " ")
    data['línea_credito'] = data['línea_credito'].str.lower()
    data['línea_credito'] = data['línea_credito'].str.strip()

    data['fecha_homologada'] = pd.to_datetime(data['fecha_de_beneficio'], dayfirst=True, errors='coerce')
    sin_id = data['fecha_homologada'].isnull()
    data.loc[sin_id, 'fecha_homologada'] = pd.to_datetime(data.loc[sin_id, 'fecha_de_beneficio'], format="%Y/%m/%d", errors='coerce')
    
    data.drop(columns='fecha_de_beneficio', inplace=True)
    data.rename(columns={'fecha_homologada':'fecha_de_beneficio'}, inplace=True)

    data.drop_duplicates(inplace=True)

    output_directory = os.path.join('files', 'output')
    output_file = os.path.join(output_directory, 'solicitudes_de_credito.csv')
    os.makedirs(output_directory, exist_ok=True)
    data.to_csv(output_file, sep=';')

    return

pregunta_01()