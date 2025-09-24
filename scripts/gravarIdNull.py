import sqlite3

conn = sqlite3.connect("../dataBase/BD_ORIGIN.db")
cursor = conn.cursor()

Id_Keywords=[]
Id_Register_Null = []
# Exemplo de query
cursor.execute("PRAGMA table_info(minha_tabela);")

# Mostrar resultados
for row in cursor.fetchall():
    Id_Keywords.append(row[1])

print("Carregando registros nullos...")
for colum in Id_Keywords: 
    cursor.execute("Select codigo FROM minha_tabela WHERE {} is NULL ;".format(colum))
    for row in cursor.fetchall():
        if row[0] in Id_Register_Null:
            break
        else:
            Id_Register_Null.append(row[0])


for cod in Id_Register_Null:
    with open("idsNull.txt", "a") as f:
        f.write("{}.\n".format(cod))
    
conn.close()
