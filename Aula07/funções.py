# Funções

'''
Funções são algoritmos criados com o objetivo de executar uma cadeia de comandos que podem/vão se repetir várias vezes no programa fazendo assim não ter a nescessidade de recriar o algoritmo toda vez que precisar repeti-lo apenas chamando a execução da função desejada.
'''

# Como criar uma função. Para criar uma função basta digitar o comando "def" logo em seguida passar o nome da função colocar "()" e finalizar a linha com ":" EX.: def Pular():

#Dica: Tente diferenciar suas funções de variáveis como por exemplo fazendo suas funções sempre começar com letras maiúsculas e variáveis sempre com minúsculas

def Boas_vindas():
    print('Bem-vindo à Ctrl+Play')

#Para executar uma função basta chama-la da seguinte forma

Boas_vindas()

#Os parenteses de um função é a região de parâmetros, que são informações que a função precisa para ser executada como por exemplo, uma função de somar necessita de dois números para poder realizar os cálculos

def Saudacao(nome):
    print('Saudações '+nome+', como está a aula de hoje?')

Saudacao('Pedro')

def Velocidade(distancia,tempo=1.5):
    velocidade = distancia/tempo
    print(f'A sua velocidade foi de {velocidade:.2f}Km/h')

#d = int(input("Digite quantos Km de distancia percorrida: "))
#t = int(input("Digite em quantas horas fez o percurso: "))

#Velocidade(d,t)
#Velocidade(tempo=t,distancia=d)

#Valor arbitrário é quando você quer passar para uma função vários valores porém não sabe a quantidade exata de valores que vai passar, para isso basta colocar o '*' antes do nome do parâmetro

def Prepara_acai(*ingredientes, tamanho='médio'):
    print(f'Preparando um Açaí {tamanho}, com os seguintes ingredientes adicionais: ')
    for ingrediente in ingredientes:
        print(f'- {ingrediente}')

Prepara_acai('banana','granola')
Prepara_acai('morango','kiwi','leite em pó',tamanho='grande')
Prepara_acai('banana',tamanho='pequeno')
Prepara_acai()

#Funções Compostas → São funções que chamam outras funções em suas definições

def Menor(lista):
    menorValor = lista[0]
    for x in lista:
        if(x < menorValor):
            menorValor=x
    return menorValor

def Maior(lista):
    maiorValor = lista[0]
    for x in lista:
        if(x > maiorValor):
            maiorValor=x
    return maiorValor

def Maior_Menor(lista):
    print(f'Maior: {Maior(lista)}')
    print(f'Menor: {Menor(lista)}')

Maior_Menor([4,5,6,2,1,3])

#Funções Recursivas → São funções que dentro da sua definição elas chamam a si mesma para ser executadas

def DobraLencol(lencol:int,gaveta:int):
    if(lencol<gaveta):
        return 0
    else:
        return 1 + DobraLencol(lencol/2,gaveta)
    
l = DobraLencol(200,25)
print(l)