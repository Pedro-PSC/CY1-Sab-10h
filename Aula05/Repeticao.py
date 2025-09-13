# FOR

'''
for item in lista:
    código que vai se repetir

for número in lista:
    print(número);
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numeros:
    print(num)

jogos = ["minecraft", "celeste", "fifa", "pokemon go", "god of war"]

for aleatorio in jogos:
    print(aleatorio)

for num in range(1, 20):
    print(num)

for numero in range(1, 20):
    if((numero % 2) != 0):
        print(numero)

for letras in "qualquer string":
    print(letras)

print("Selecione o valor que você quer jogar:")
for valor in range(2, 10):
    print(f"R$ {valor},00")

# WHILE

'''
while condição:
    Código que será repetido enquanto a condição for verdadeira
'''

contador = 1
while contador < 10:
    print("Contando:", contador)
    contador += 1

senha = " "
while senha != "5221":
    senha = input("Digite a senha:")
print("Acesso liberado")

soma = 0
numeros = range(1, 1000)
i=0
while soma < 200:
    soma += numeros[i]
    i+=1
print(soma)

# CONTROLANDO LOOPS COM BREAK, CONTINUE E PASS

'''
*NÃO EXISTE NO PYTHON MAS EM OUTRAS LINGUAGENS*
do: 
    codigo q vai repetir
while condição de parada

while condição:
    código
    if teste1:
        break
    if teste2:
        continue
    else:
        pass
'''

for i in range(1, 10):
    if i == 3:
        continue

    if i == 5:
        print("Encontrado o número 5, parando o loop (break)")
        break

    if i == 2:
        pass

    print(f"Número atual: {i}")

