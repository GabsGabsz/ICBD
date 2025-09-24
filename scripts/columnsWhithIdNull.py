import sqlite3
import lerIdNulos
import showTableId
import json

conn = sqlite3.connect("../dataBase/BD_ORIGIN.db")
cursor = conn.cursor()

columnNullById = []
idKeys = showTableId.getKeyWordsTable()
idNulls = lerIdNulos.lenIdNull()
count = 1
with open("columnsNull.txt", "a") as f:
    for id in idNulls:
        print("FILTRANDO E GRAVANDO REGISTROS {} de {}...".format(count,len(idNulls)))
        idF = id.replace(".","")
        vet = []
        for column in idKeys:
            cursor.execute("SELECT {} FROM minha_tabela WHERE codigo = {}".format( column, idF))
            for row in cursor.fetchall():
                if row[0] == None:
                    vet.append(column)
        f.write("{}.\n".format([idF, vet]))
        count += 1
        print("---------------------------------------------------------------------------------------")
        print(columnNullById)
        print("---------------------------------------------------------------------------------------")
             
print(columnNullById)
