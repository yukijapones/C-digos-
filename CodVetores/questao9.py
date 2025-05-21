print ("Calculo de numeros reias, quantidade de numeros negativos e a soma dos positivos.")

n0 = int(input("coloque o 1 numero do vetor:  "))
n1 = int(input("coloque o 2 numero do vetor:  "))
n2 = int(input("coloque o 3 numero do vetor:  "))
n3 = int(input("coloque o 4 numero do vetor:  "))
n4 = int(input("coloque o 5 numero do vetor:  "))
n5 = int(input("coloque o 6 numero do vetor:  "))
n6 = int(input("coloque o 7 numero do vetor:  "))
n7 = int(input("coloque o 8 numero do vetor:  "))
n8 = int(input("coloque o 9 numero do vetor:  "))
n9 = int(input("coloque o 10 numero do vetor:  "))

numVetor = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]
print (numVetor)

indice = 0
quantNegativos = 0
somaPositivos = 0

while indice < 10:

    if numVetor[indice] < 0:
        quantNegativos += 1
         
    elif numVetor[indice] > 0:
        somaPositivos += numVetor[indice]
    indice += 1 

print ("A quantidade de numeros negativos no vetor apresentado é:   ", quantNegativos)
print ("A soma dos numeros positivos que sobraram no vetor é:   ", somaPositivos)










