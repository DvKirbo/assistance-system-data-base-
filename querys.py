import pandas as pd
import sqlite3 as sql

def create_db():
    conn =sql.connect("alumnos.db")
    conn.commit()
    conn.close()

def create_table ():
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE personas(
                       codigos integer, 
                       nombres text,
                       estado text
                   )
                   """)
    
    conn.commit()#subimos cambios
    conn.close()#cerramos conexion
    
def mostrar():
    conn=sql.connect("alumnos.db")
    cursor= conn.cursor()
    cursor.execute(""" SELECT * FROM personas """)
    datos= cursor.fetchall()
    conn.commit()
    conn.close()
    a,b,c=datos
    print(a,b,c)

def update (cod):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute (f"""UPDATE personas SET estado = "PRESENTE" WHERE codigos = {cod} """)
    conn.commit()
    conn.close()
    
#create_db()
#create_table()
update()