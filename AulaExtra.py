
print("1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")

operacao = int(input("Escolha a sua operação: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    resultado = num1 * num2
elif operacao == 4:
    resultado = num1 / num2
else:
    print("Você precisa escolher uma operação entre 1 e 4")
print(resultado)
