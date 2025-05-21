print ("Digite 5 valores e veja o programa mostrando aonde esta o maior e menor valor no vetor.")

n0 = int(input("Digite o 1 numero:   "))
n1 = int(input("Digite o 2 numero:   "))
n2 = int(input("Digite o 3 numero:   "))
n3 = int(input("Digite o 4 numero:   "))
n4 = int(input("Digite o 5 numero:   "))

valorVetor = [n0,n1,n2,n3,n4]
print (valorVetor)

indice = 1 
maior = valorVetor[0]
menor = valorVetor[0]
posiMaior = 0
posiMenor = 0

while indice < 5:
    if valorVetor[indice] > maior:
        maior = valorVetor[indice]
        posiMaior = indice
    elif valorVetor[indice] < menor:
        menor = valorVetor[indice]
        posiMenor = indice

    indice += 1

print ("O maior valor do vetor é",maior, "se encontra na posicao:  ", posiMaior)
print ("O menor valor do vetor é",menor," se encontra na posicao:  ", posiMenor)