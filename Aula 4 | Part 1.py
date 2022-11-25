#1o. passo: importar a biblioteca sqlite3
import sqlite3

conexao = sqlite3.connect("dc_universe.db")

cursor = conexao.cursor()

  #4o. passo: Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

cursor.execute(sql)

pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
  
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")


  






