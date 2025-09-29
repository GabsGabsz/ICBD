import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


# Exemplo de query
#cursor.execute("SELECT * FROM general;")
# Mostrar resultados
#for row in cursor.fetchall():
    #print(row)
#conn.close()