"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.

"""

import pandas as pd

def ingest_data():

    with open('clusters_report.txt', 'r') as file:
        data = []
        for i, line in enumerate(file):
            if i >= 5:  # Las líneas se cuentan desde 0, por lo que la línea 5 es la línea 4 en la cuenta de Python
                columns= line.split()  # Dividir la línea en palabras y agregarla a la lista de datos
                if len(columns) >=1: # Si la línea tiene al menos una palabra, se puede dividir en columnas
                    try:
                        cluster = columns[0] # El cluster es un número
                        cantidad_de_palabras_clave = int(columns[1]) # La cantidad de palabras clave es un número
                        porcentaje_de_palabras_clave = columns[2] # El porcentaje de palabras clave es una palabra seguida de un número
                        principales_palabras_clave= ' '.join(columns[4:]) # Las palabras clave son todas las palabras restantes en la línea
                        data.append([cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave])
                    except:
                        if len(data) > 0:
                            principales_palabras_clave= ' '.join(columns)
                            data[len(data)-1][3] += ' ' + principales_palabras_clave 

    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',','.').astype(float)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.','')
    df.columns= df.columns.str.replace(' ', '_').str.lower()
    return df
#print(ingest_data())            

