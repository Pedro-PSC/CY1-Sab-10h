# Strings é um tipo de variável que armazena textos. Para utilizar uma string basta declarar uma variável e passar como valor o texto que deseja salvar entre '' ou ""

texto = 'Ctrl+Play-  Escola de Programação e Robótica'

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
print(nome[::2])