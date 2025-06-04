def soma_operacao(valores):
    return sum(valores)

def subtracao_operacao(valores):
    return valores[0] - valores[1]

def multi_operacao(valores):
    return valores[0] * valores[1]

def div_operacao(valores):
    return valores[0] / valores[1]

print("Bem-vindo a calculadora do Yuki!!")

while True:

    valor1 = int(input("Digite o primeiro numero:   "))
    valor2 = int(input("Digite o segundo numero:    "))

    valores = [valor1, valor2]

    print("Qual operacao deseja para executar a conta?")
    operacao = int(input(f"{1}- Soma , {2}- Subtracao , {3}- Multiplicacao , {4}- Divisao , {5} encerrar a calculadora:   "))



    if operacao == 1:
        resultado = soma_operacao(valores)
        print(f"Resultado da soma: {resultado}")

    elif operacao == 2:
        resultado = subtracao_operacao(valores)
        print(f"Resultado da subtração: {resultado}")

    elif operacao == 3:
        resultado = multi_operacao(valores)
        print(f"Resultado da Multiplicacao: {resultado}")

    elif operacao == 4:
        resultado = div_operacao(valores)
        print(f"Resultado da divisao: {resultado}")

    elif operacao == 5:
            print("Encerrando a calculadora. Até logo!")
            break

    else:
        print("Operacao invalida!!")

    print(valores)





