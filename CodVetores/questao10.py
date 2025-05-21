print ("digite 5 numeros a seguir.")

n0 = int(input("digite o 1 numero:   "))
n1 = int(input("digite o 2 numero:   "))
n2 = int(input("digite o 3 numero:   "))
n3 = int(input("digite o 4 numero:   "))
n4 = int(input("digite o 5 numero:   "))

valorNum = [n0,n1,n2,n3,n4]
print (valorNum)

indice = 1 
valorMaior = valorNum[0]
conta = valorNum[0]

while indice < 5:

    if valorNum[indice] > valorMaior:
        valorMaior = valorNum[indice]

    indice += 1 
conta = valorNum[0] / 5

print ("O maior valor do vetor apresentado é:   ", valorMaior)
print ("O menor valor do vetor apresentado sendo a media é:   ", conta)



    



