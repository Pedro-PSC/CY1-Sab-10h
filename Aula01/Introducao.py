print('Olá Mundo')

# isto é um comentário de uma linha

'''
isto é
um comentário
de múltiplas
linhas
'''

# Os tipos de dados numérios são: Int → inteiros | Float → Decimais

# Para verificar o tipo do número usa-se o comando type() e como parâmetro passa o número dentro do parenteses

print(type(3))
print(type(1.5))

'''
+ → adição
- → subtração
/ → divisão
* → multiplicação
**→ potência
'''

#Adição
print(1+4)

#Subtração
print(5-3)

#Divisão
print(14/7)

# Multiplicação
print(4*3)

# Potência
print(2**3)

# Ordem das operações em Python igual na matemática
print(2 + 10 * 10 - 5)

# Você pode use parênteses para especificar a ordem
print((2+10) * (10-5))

# Varáveis são uma forma de salvar dados no programa para serem utilizados no momento nescessário, elas recebem esse pois podem variar de tipo e valor

'''
Regras de declaração em variáveis
1ª → O nome deve ser único
2ª → Não pode conter caracteres especiais
3ª → Não pode conter espaço em nome composto
4ª → Não pode começar com números
'''

# Declarando uma variável
numero = 10
resultado = numero + numero
print(resultado)

# Está substituindo o valor da variável numero e não criando uma nova variável
numero = 30
# O novo valor de resultado é o valor antigo mais o valor de numero
resultado = resultado + numero
print(resultado)


