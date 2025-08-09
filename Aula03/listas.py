# Lista é uma forma de salvar várias informações em um único lugar, ou seja vários dados em uma única variável

# As mesmas regras de declaração de variáveis se aplicam a listas
# O [] é o simbolo que representa lista
 
convidados = ['Frederico','Davi','Alexandre','Beatriz','Pedro']
print(convidados)

print("Primeiro convidado da festa: "+convidados[0])

# Diferente das strings as listas são mutáveis.

convidados[-1] = 'Sheila'
print(convidados)

# uma das formas de adicionar elementos na nossa lista é usar a função append() e passar como parâmetro o item que quer inserir. Esse comando SEMPRE vai adicionar o novo elemento no final da lista.

convidados.append('Pedro')
print(convidados)

# Outra forma de adicionar itens na lista é atravez do comando insert(), onde nele passa como parâmetro a posição na qual se deseja inserir o item na lista e qual o item que deseja inserir.

convidados.insert(2,'Thiago')
print(convidados)

# Para remover um elemento da lista existe três formas, 'del', 'pop()', 'remove()'

del convidados[0]
print(convidados)

# o pop() ele remove o item da lista mas te da a opção de salvar esse item em uma variável específica, se não passar um index para o pop() ele vai remover o último item da lista

convidadoRevomido = convidados.pop(3)
print(convidados)
print(convidadoRevomido+' foi expulso(a) da festa')

# O remove() ele elimina o elemento da lista através de uma busca

viajando = 'Alexandre'

convidados.remove(viajando)
print(convidados)

convidados.append('Frederico')
convidados.append('Beatriz')
convidados.append('Alexandre')

# Para organizar uma lista existem 3 formas: sort(), sorted(), reverse()
# O comando sort() ele organiza em crescente ou alfabética

convidados2 = convidados[:]

print(convidados2)
convidados2.sort()
print(convidados2)

# Caso você queira a ordem alfabética inversa ou decrescente passa como parâmetro para o sort(reverse=True)

convidados2.sort(reverse=True)
print(convidados2)

# O comando sorted faz a mesma coisa que o comando sort, porém ele não é destrutivo ou seja ele não altera a informação da lista de fato é apenas para exibição

print(convidados)
print(sorted(convidados))
print(convidados)

# O Reverse() exibe a lista de trás pra frente

print(convidados)
convidados.reverse()
print(convidados)