#region Tuplas

# Tuplas são "listas" cujos valores após insersão não podem ser alterados como por exemplo uma lista com os dias da semana.

# Para criar uma tupla basta fazer igual uma lista mas ao invés de [] usamos () e separamos os elementos com a ,

print("Tuplas\n")

t = ("Dom","Seg","Ter","Qua","Qui","Sex","Sáb")
print(t)
t = ("Dom","Seg","Ter","Qua","Qui","Sex","Sáb","Lan")
print(t)

# Na hora de buscar um dado na tupla em um index específico usamos [] igual usamos em listas e strings

print(t[2])
print(t[2:5])

# Métodos que funcionam com tuplas

# len() para retornar o tamanho
print(len(t))

# index() para retornar em qual índice está o elemento
print(t.index('Ter'))

#endregion

#region Conjuntos(sets)

print("\nConjutos Sets\n")

# Conjuntos sets são "Listas" mutáveis (Podem ser alteradas) porem não podem repetir o mesmo valor dentro dela

# Para criar um conjunto basta criar uma variável que vai receber esse conjunto e após o sinal de = escrever set()

x = set()

# Para adicionar elementos ao conjunto basta usar o método add() e como parâmetro passar o elemento que deseja inserir

x.add(1)
x.add(2)
print(x)
x.add(1)
print(x)

# Todos os métodos que funciona nas tuplas também funciona nos conjuntos
#endregion

#region Dicionários

# Um dicionário é uma estrutura de dados que armazena as informações em pares de chave-valor. Ela permite acesso rápido e fácil dos valores a partir de suas respectivas chaves.

# Para criar um dicionário, use o simbolo de {} após declarar a variável. Um dicionário é uma coleção de pares chave-valor.

print("\nDicionário\n")

meu_dicionario = {
    "nome" : "Pedro",
    "idade" : 27,
    "cidade" : ["Lagoa Santa"]
    }

# Acessando valores em um dicionário
# Para acessar um valor, use a chave correspondente
print(meu_dicionario["nome"])
print(meu_dicionario["idade"])
print(meu_dicionario["cidade"])

# Para adicionar um valor em uma chave
meu_dicionario["cidade"].append("Belo Horizonte")
print(meu_dicionario["cidade"])

# Para adicionar uma nova chave-valor ao dicionário
meu_dicionario["profissao"] = "Professor"
print(meu_dicionario)

# Para modificar o valor de uma chave existente
meu_dicionario["idade"] = 26
print(meu_dicionario["idade"])

# Para remover uma chave-valor do dicionário
del meu_dicionario["cidade"]
print(meu_dicionario)

# Iterando sobre um dicionário
# Podemos percorrer todas as chaves ou valores do dicionário:
for chave in meu_dicionario:
    print(f"Chave: {chave}, Valor: {meu_dicionario[chave]}")

# Métodos.keys(), .values() e .items()
print(meu_dicionario.keys()) # Retorna todas as chaves do dicionário
print(meu_dicionario.values()) # Retorna todos os valores do dicionário
print(meu_dicionario.items()) # Retorna todos os pares chave-valor do dicionário

# Verificando se uma chave existe no dicionário
if "nome" in meu_dicionario:
    print("A chave 'nome' está presente no dicionário.")

# Limpando o dicionário
meu_dicionario.clear() # Remove todos os items do dicionário
print(meu_dicionario)
#endregion