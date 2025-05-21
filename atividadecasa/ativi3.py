num = int(input("Digite um numero de 1 a 10 para obter a tabuada do numero: "))

if 1 <= num <= 10:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Número fora do intervalo permitido.")