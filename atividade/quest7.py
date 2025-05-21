import random 

numero = list(range(1, 101))

lista = []

for i in numero:
    if i % 2 == 0:
        lista.append(i)

print ("-----------------------------------------")
print ("Os numeros PARES da lista de 1 a 100 sao:")
print (lista)
print ("-----------------------------------------")