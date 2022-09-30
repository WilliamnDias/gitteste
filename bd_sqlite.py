import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("William Novaes", 80.5)')
# conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)






cursor.close()
conexao.close()