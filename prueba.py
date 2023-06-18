import pandas as pd
import sqlite3 as sql
 
conn = sql.connect("alumnos.db")
df= pd.read_sql("SELECT * FROM personas", conn)
print(df.head())
print(df["nombres"][0])
n= df.shape[0]#numero de filas

for i in range (n):
    codigo = df["codigos"][i]
    nombre = df["nombres"][i]
    estado = df["estado"][i]
    print(codigo, nombre, estado)
    #kirb_lore[1]["alumnos"].append({f"{codigo}":[{"nombre":nombre},{"estado":estado}]})

