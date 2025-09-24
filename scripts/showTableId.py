import sqlite3

conn = sqlite3.connect("../dataBase/BD_ORIGIN.db")
cursor = conn.cursor()

def getKeyWordsTable():
    Id_Keywords=[]
    # Exemplo de query
    cursor.execute("PRAGMA table_info(minha_tabela);")

    # Mostrar resultados
    for row in cursor.fetchall():
        Id_Keywords.append(row[1])
    print(Id_Keywords)
    return Id_Keywords
