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



