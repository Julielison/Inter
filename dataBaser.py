import sqlite3

conn = sqlite3.connect('usersData.db')

cursor = conn.cursor()

cursor.execute("""               
CREATE TABLE IF NOT EXISTS Users (
               Id TEXT NOT NULL PRIMARY KEY,
               User TEXT NOT NULL,
               Password TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados")