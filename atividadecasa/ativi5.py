numeros = [10,2,3,16,17,19,4,7,1,11]

pares = 0
impares = 0

for i in numeros:
    if i % 2 == 0:
        pares += 1 
    else:
        impares += 1 

print ("A quantidade de numeros pares sao:  ", pares)
print ("A quantidade de numeros impares sao:  ", impares)

