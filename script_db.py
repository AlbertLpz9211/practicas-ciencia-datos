import sqlite3
import pandas as pd

conexion = sqlite3.connect('agrocorita.db')
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS monitoreo (
    id TEXT PRIMARY KEY,
    cultivo TEXT,
    humedad REAL
    )
""")

for _, fila in pd.read_csv('datos_campo.csv').iterrows():
    cursor.execute("""
    INSERT OR REPLACE INTO monitoreo (id, cultivo, humedad)
    VALUES (?, ?, ?)
    """, (fila['id_parcela'], fila['cultivo'], fila['humedad']))

if conexion:
    conexion.commit()
    conexion.close()
print("Base de datos creada y datos insertados correctamente.")




