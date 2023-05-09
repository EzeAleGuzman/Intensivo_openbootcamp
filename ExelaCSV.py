import pandas as pd

# Leer el archivo Excel y convertirlo a DataFrame
df = pd.read_excel('archivo.xlsx')

# Guardar el DataFrame en un archivo CSV
df.to_csv('archivo.csv', index=False)