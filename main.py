# AULA 1
# Meu primeiro projeto Pyton
# print () = comando de saída
print ("Hello world!")

# Quando quiser guardar uma string
nome = "Camila Luiz"
# Quando quiserem guardar um código
idade = 24

print (nome)

# Frase 'minha idade é'
print ("Meu nome é " +nome)
print("Minha idade é "+str(idade))
print (f"Minha idade é {idade}")
print ("Minha idade é {}".format(idade))
print ("\n")

# Quando quiser exibir tudo junto
print("Meu nome é {} e eu tenho {} anos!".format(nome,idade))

print ("\n")

# AULA 2
# Comando input: permitir que o usuário digite algo
nome = input("Digite seu nome: ")

# Comando de saída (exibir na tela)
print ("Boa noite, seu nome é {}".format(nome))
print ("\n")
idade = int(input("Digite sua idade: "))
print ("{}, você tem {} anos, muito prazer!".format(nome,idade))

# Caso queira dobrar a idade
dobro = idade*2
print ("O dobro da sua idade seria {}".format(dobro))

# Estrutura por condição
if idade >= 18:
  print("Você é maior de idade! Já pode beber ou dirigir")
else:
  print("Você é muito jovem para beber...")
  
print ("\n")
  
  # Gênero: Feminino, Masculino, Prefiro não Identificar
genero = input("Informe o gênero M=Masculino, F=Feminino ou X=Prefiro Não Identificar: ")
print ("Tudo bem!, seu nome é {}, você tem {} anos e seu genero é {}".format(nome, idade, genero))

if idade >= 18 and genero == "M":
  print("... e você também precisa/precisou prestar o serviço militar obrigatório")

  print ("\n")

  # Nome do aluno e nota (de 0 a 10) e, se ele tirou nota 10, mostra "{nome}, você é bichão, mesmo..."
nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))

if (nota == 10):
  print(f"{nome}, você é muito bom, parabéns!")
elif (nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho")
else: # é sempre automaticamente o que as duas condições não tratamento
  print("Que pena, tente da próxima vez...")


print ("\n")
print ("\n")

# AULA 3
  
# Exibir de 1 até 10

contador = 1
while ( contador <= 10):
  print (contador)
  contador = contador+1

print ("\n")

# Laço
fruta = "Morango"
print(fruta)

fruta1 = "Morango"
fruta2 = "Laranja"
fruta3 = "Pêra"

# Lista
frutas = ["Morango", "Laranja", "Pêra"]
print ("\n")

# Mostrar todas
print(frutas)
print ("\n")
# Somente a terceira
print(frutas[2])
print ("\n")

# Exibir quantas frutas tem na minha lista
print ("Quantidade de frutas:")
print (len(frutas))
print ("\n")

#Quero incluir uma fruta nova
frutas.append("Banana")

print(len(frutas))
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])
print ("\n")
print("Exemplo das frutas com while..")
frutas.append("Uva")

i=0 #(i de index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1
  
print ("\n")
print("Exemplo das frutas com FOR")
for fruta in frutas:
    print(fruta)

print ("\n")

# Criando Funções

preco = 1999.90

# Calcular apenas 5% de imposto

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

# Criar uma função calcular_imposto()
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função (7%): {imposto}")

# Explicação de variável local x global
print(preco) 
preco_produto = 100
print(preco_produto) 


# Agora calcular imposto a alíquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")


# Declarar um função calcular_imposto_aliquota que recebe dois parâmetros
  
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

# E se agora o imposto for 10%?
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")


# AULA 4

import sqlite3

def conectar():
  #2o. passo: Vamos estabelecer uma
  #conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")
  
  cursor = conexao.cursor()

sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

cursor.execute(sql)

pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
  
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")


# OU 


import sqlite3

conexao = sqlite3.connect("dc_universe.db")

cursor = conexao.cursor()

sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"


cursor.execute(sql)

conexao.commit()
conexao.close()

# OU 

con, cur = bd.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)

con.commit()
con.close()


# OU


import aula4_2022_11_16c as bd

con, cur = bd.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

#Consulta aqui a tabela grupos e exibe na tela, pedindo para o usuário digitar o grupo_id


#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)

#Insert pessoas_grupos
#INSERT INTO pessoas_grupos (pessoa_id, grupo_id) VALUES (X, X)

con.commit()
con.close()