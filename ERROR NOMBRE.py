import sqlite3
from datetime import date, timedelta


database = "C:\Program Files\lonchepos1.1.0_w10\database.db"
connection = sqlite3.connect(database)

cursor = connection.cursor()

def fetchData(folio):
    query = "SELECT total, hora, cancelado, nombre FROM tickets WHERE folio = '{}';".format(folio)
    cursor.execute(query)
    data = cursor.fetchall()[0]
    return data

def modifyName(oldName, newName):
    verification = input("SEGURO QUE QUIERES CAMBIAR EL NOMBRE DE '{}' A '{}'? (s/n)".format(oldName, newName))
    if verification == "s" or verification == "S" or verification == "SI" or verification == "si":
        query = "UPDATE tickets SET nombre = '{}' WHERE folio = '{}';".format(newName, folio)
        cursor.execute(query)
        connection.commit()
        input("EL NOMBRE AHORA ES: {}".format(fetchData(folio)[3]))
    else:
        input("EL NOMBRE NO FUE MODIFICADO")
        exit()
        
    
    

folio = input("ESCRIBE EL FOLIO QUE QUIERES MODIFICAR: ")

data = fetchData(folio)

total = data[0]
hora = data[1]
status = data[2]
oldName = data[3]

if oldName == "" or oldName == None:
    respuesta1 = input("EL TICKET {} NO TIENE NINGUN NOMBRE REGISTRADO, QUIERES MODIFICARLO?(s/n)".format(folio))
else:
    respuesta1 = input("EL TICKET {} ESTA A NOMBRE DE '{}', QUIERES MODIFICARLO?(s/n)".format(folio, oldName))

if respuesta1 == "s" or respuesta1 == "S" or respuesta1 == "SI" or respuesta1 == "si":
    modifyName(oldName, input("ESCRIBE EL NUEVO NOMBRE: "))
else:
    input("EL NOMBRE NO FUE MODIFICADO")
    exit()

