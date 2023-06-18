import sqlite3 as sql
from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd

        

#llenando datos de la api para los alumnos

kirb_lore = [{
    'code':200,
    'status':'ok👌'
},
             
{
    'alumnos':[
        
    ]
}
    ]



conn = sql.connect("alumnos.db")
df= pd.read_sql("SELECT * FROM personas", conn)

n= df.shape[0]#numero de filas

for i in range (n):
    codigo = df["codigos"][i]
    nombre = df["nombres"][i]
    estado = df["estado"][i]
    kirb_lore[1]["alumnos"].append({f"{codigo}":[{"nombre":nombre},{"estado":estado}]})

for clave in kirb_lore[1]["alumnos"]:
    for i in clave:
        print(i)
    #print(clave) 


app = Flask(__name__)

@app.route('/kirb_api')
def status():
    return jsonify (kirb_lore[0])




@app.route('/kirb_api/main')
def main():
    return jsonify(kirb_lore[1])
    

@app.route('/kirb_api/main/<ru>')
def rutas(ru):
    print(ru)
    j=0
    for clave in kirb_lore[1]["alumnos"]:
        for i in clave:
            if (i == ru):
                print("hola")
                #cambiando estado a presente
                kirb_lore[1]["alumnos"][j][str(i)][1]["estado"]="PRESENTE"
                print(kirb_lore[1]["alumnos"][j][str(i)][1]["estado"])
                return jsonify(kirb_lore[1]["alumnos"][j])
        j+=1
       #         print(i)
                #return jsonify(kirb_lore[1])
    

    
#if __name__ == '__name__':
app.run(debug=True)    


def modificar ():
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute(""" """)


#de ahi modificarlo para q mostrar opcion de un solo alumno