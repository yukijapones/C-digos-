num0 = int(input("Digite o 1 numero: "))
num1 = int(input("Digite o 2 numero: "))
num2 = int(input("Digite o 3 numero: "))
num3 = int(input("Digite o 4 numero: "))
num4 = int(input("Digite o 5 numero: "))
num5 = int(input("Digite o 6 numero: "))
num6 = int(input("Digite o 7 numero: "))
num7 = int(input("Digite o 8 numero: "))
num8 = int(input("Digite o 9 numero: "))
num9 = int(input("Digite o 10 numero: "))

numVetor = [num0,num1,num2,num3,num4,num5,num6,num7,num8,num9]

for i in range(10):
    for j in range(i + 1, 10):
        if numVetor[j] < numVetor[i]:
            aux = numVetor[i]
            numVetor[i] = numVetor[j]
            numVetor[j] = aux

print("Números em ordem crescente:")
print(numVetor)