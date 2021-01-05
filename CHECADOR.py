import sqlite3
from datetime import date, timedelta


database = "C:\Program Files\lonchepos1.1.0_w10\database.db"
connection = sqlite3.connect(database)

cursor = connection.cursor()

def fetchData(folio):
    query = "SELECT total, hora, nombre, notas FROM tickets WHERE folio = '{}';".format(folio)
    cursor.execute(query)
    ticket = cursor.fetchall()[0]
    query = "SELECT producto, cantidad FROM ticketProducts WHERE folio = '{}';".format(folio)
    cursor.execute(query)
    ticketProducts = cursor.fetchall()
    return [ticket, ticketProducts]
while True:
    folio = input("ESCRIBE EL FOLIO QUE QUIERES CHECAR: ")
    data = fetchData(folio)
    print("FOLIO: {}".format(folio))
    print("TOTAL: {}".format(data[0][0]))
    print("HORA: {}".format(data[0][1]))
    print("")
    print("NOMBRE: {}".format(data[0][2]))
    print("NOTAS: {}".format(data[0][3]))
    print("")
    print("PRODUCTOS: ")
    for i in range(len(data[1])):
        print(data[1][i])
    print("________________________________________")
