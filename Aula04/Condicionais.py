#Condicionais → São estruturas de código que só executam em determinadas situações

'''
estrutura base de condicional

if condição:
    código
'''

# Operadores lógicos

'''
== → igualdade | Ex.: (10 == 10 = True) ou (10 == 8 = False)
!= → desigualdade | Ex.: (10 != 10 = False) ou (10 != 8 = True)
> → maior que | Ex.: (10 > 10 = False) ou (10 > 8 = True)
< → menor que | Ex.: (10 < 10 = False) ou (10 < 18 = True)
>= → maior ou igual que | Ex.: (10 >= 10 = True) ou (10 >= 8 = True)
<= → menor ou igual que | Ex.: (10 <= 10 = True) ou (10 <= 18 = True)
'''

# Comparadores Lógicos

'''
and (&&) → Retorna verdadeiro se todos os resultados fores verdadeiros
or (||) → Retorna verdadeiro se apenas um dos resultados for verdadeiro
not (!) → Ele busca o oposto
'''


nota = float(input("Insira a nota do aluno: "))

if nota >= 6:
    print(f'Aluno aprovado com nota: {nota}')
elif nota > 3 and nota < 6:
    print(f'Aluno de recuperação com nota: {nota}')
else:
    print(f'Aluno de reprovado com nota: {nota}')