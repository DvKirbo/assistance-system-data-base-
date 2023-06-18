import pandas as pd
import sqlite3 as sql

path_ = "./alumnos.xlsx"
dp = pd.read_excel(path_, sheet_name='Hoja1')

print(dp.head())
print(dp.tail())
print(dp.shape)
print(dp.dtypes)
print(dp.describe())
print(dp.columns)

#obteniendo id
print(dp["Codigo"])
print('asdsdasadasd')
print(dp.count(axis=0))
#print(dp["ALUMNO"][1])
print(dp.shape[0])#numero de filas

print(dp['Codigo'][0])



conn = sql.connect("alumnos.db")
cursor = conn.cursor() 
for i in range (38):
    codigo=dp["Codigo"][i]
    nombre =dp["ALUMNO"][i]
    estado = "AUSENTE"
    cursor.execute (f"""INSERT INTO personas VALUES ({codigo}, "{nombre}", "{estado}")""")
    conn.commit()
conn.close()



#creacion de tablas