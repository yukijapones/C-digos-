print("calculadora")

operacao = int(input("Insira a operação que deseja: 1. Soma, 2. Subtração, 3. Divisão, 4. Multiplicação "))

a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))

if operacao == 1:
    soma = a + b
    print("Resultado:", soma)
elif operacao == 2:
    subtracao = a - b
    print("Resultado:", subtracao)
elif operacao == 3:
    divisao = a / b
    print("Resultado:", divisao)
elif operacao == 4:
    multiplicacao = a * b
    print("Resultado:", multiplicacao)
else:
    print("Operação inválida!")