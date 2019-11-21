import sqlite3

connection = sqlite3.connect('SQLite/test.db')

cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS pessoa(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, idade INT, cidade TEXT)')

nome = 'Eduardo'
idade = 18
cidade = 'São Paulo'

cursor.execute('INSERT INTO pessoa VAlUES(?, ?, ?)', (nome, idade, cidade))

connection.commit()

cursor.execute("SELECT * FROM PESSOA")

for linha in cursor.fetchall():
  print(linha)

""" connection.close()
cursor.close() """
