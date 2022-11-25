#1o. passo: importar a biblioteca sqlite3
import sqlite3

conexao = sqlite3.connect("dc_universe.db")

cursor = conexao.cursor()

  #4o. passo: Comando SQL do banco
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"
print(cursor.execute(sql))