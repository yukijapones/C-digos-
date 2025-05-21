numA0 = int(input("digite o 1 numero no vetor A:    "))
numA1 = int(input("digite o 2 numero no vetor A:    "))
numA2 = int(input("digite o 3 numero no vetor A:    "))
numA3 = int(input("digite o 4 numero no vetor A:    "))
numA4 = int(input("digite o 5 numero no vetor A:    "))

vetorA = [numA0,numA1,numA2,numA3,numA4]
print(f"Valor de vetor A: {vetorA}")

numB0 = int(input("digite o 1 numero no vetor B:    "))
numB1 = int(input("digite o 2 numero no vetor B:    "))
numB2 = int(input("digite o 3 numero no vetor B:    "))
numB3 = int(input("digite o 4 numero no vetor B:    "))
numB4 = int(input("digite o 5 numero no vetor B:    "))

vetorB = [numB0,numB1,numB2,numB3,numB4 ]
print(f"Valor de vetor B: {vetorB}")

vetorC = []

indice = 0

for i in vetorA:
    vetorC += [vetorA[indice] + vetorB[indice]]
    indice += 1 
print (f"Valor de vetor C: {vetorC}")
