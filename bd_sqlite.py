import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()












cursor.close()
conexao.close()