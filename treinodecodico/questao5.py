vetor = [22, 36, 44, 77, 25, 29, 13, 86, 16, 38, 80]
print(vetor)

infVetor = int(input("Digite um número de 0 a 10 para verificar quantos dígitos pares tem o valor nessa posição: "))

if 0 <= infVetor <= 10:
    numero = vetor[infVetor]
    print("Número escolhido:", numero)

  
    numerosPares = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            numerosPares += 1
        numero = numero // 10

    print("A quantidade de dígitos pares é:", numerosPares)

else:
    print("valor invalido!")

