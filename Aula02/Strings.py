# Strings é um tipo de variável que armazena textos. Para utilizar uma string basta declarar uma variável e passar como valor o texto que deseja salvar entre '' ou ""

texto = 'Ctrl+Play - Escola de Programação e Robótica'

# Strings não nescessáriamente precisam estar atreladas à uma variável, no caso da exebição através da função print()

print(texto)
print('Texto impresso direto do print')

# Para saltar linhas durante a exibição de um texto se utiliza o comando '\n'

print('Saltando \n\n linhas \n !')

print('Olá\n\nlinhas\n!')

# Para dar um espaçamento entre palavras equivalente a tecla 'tab' pode-se usar o comando '\t'

print('Teste\tde\tespaçamento')

# Caso você saber qual o tamanho de uma string em relação à quantidade de caracteres basta usar a função len() passando como parâmetro a string que deseja saber a informação.

print(len(texto))

# Em uma string podemos usar o Index para utilizar apenas parte de uma string para exibições, comparações etc. Para trabalhar com Index basta após chamar a variável onde a string está salva usar o comando de '[]'

nome = 'Pedro Paulo Sousa do Couto'

print(nome[0]) # Será imprimido apenas a primeira letra da string 'P'

# A partir de um caractere

print(nome[6:]) # Paulo Sousa do Couto

# Até um caractere

print(nome[:6]) # Pedro 

# De um ponto ao outro

print(nome[12:17]) # Sousa

# usando números negativos no [] fazemos a manipulação inversa do index

print(nome[-1]) # o

#Tudo até o -6
print(nome[:-6]) # Pedro Paulo Sousa do

# Para ir saltenado de caractere a caractere na quantidade desejada
print(nome[::-2]) #PdoPuoSuad ot

# Strings são imutáveis, ou seja não é possível pegar um index e alterar somente ele
'''
NÃO PODE
nome[0] = F

PODE
nome = 'Fedro Paulo Sousa do Couto'
'''

# É possível "somar" string, o nome dado à isso é concatenação

nome2 = 'Frederico'
sobrenome2 = "Cunha"
print(nome2+' '+sobrenome2)

# É possivel repetir uma string várias vezes

print((sobrenome2+' ')*10)

# Para poder unir letras com números usamos a função str() onde ela converte qualquer outro tipo de variável para string

numeroDeIrmaos = 2
print('Você tem ' +str(numeroDeIrmaos)+ ' irmãos')

# Outra forma de poder imprimir textos junto com números é vc usar a virgula para inserir os números

print('Você tem', numeroDeIrmaos, 'irmãos')

# Por fim a última forma de imprimir textos com números é formatando a string no print

print(f'Você tem {numeroDeIrmaos} irmãos')

# Para colocar todos os caracteres em maiúsculo use a função upper()
print(nome.upper())

# Para colocar todos os caracteres em minúsculo use a função lower()
print(nome.lower())

#Para dividir uma string em palavras separadas por espaço em branco use a função slipt()
cadaPalavra = texto.split()
print(cadaPalavra)
print(cadaPalavra[0])

# Caso passe algum parâmetro no split ele irá separar com base no parâmetro passado
cadaPalavra = texto.split(' - ')
print(cadaPalavra)
print(cadaPalavra[0])

# Para receber dados vindos de um usuário basta usar o comando input(), todo valor passado por um input sempre será salvo como string

nome = input('Digite seu nome: ')
print('\nOlá',nome)