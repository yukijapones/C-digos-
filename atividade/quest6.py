import random

numeros = list(range(1, 11))

listaPar = []
listaImpar = []
juncaoLista = []

for i in numeros:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)

print (f"Lista PAR: {listaPar}")
print (f"Lista IMPAR: {listaImpar}")

soma = listaPar + listaImpar
juncaoLista = soma 

print (f"Juncao das duas listas de PAR e IMPAR: {juncaoLista}")