matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0], 
]

maior = [0][0]

for linha in range(4):
    for coluna in range(4):
        if maior < matriz [linha][coluna]:
            maior = matriz [linha][coluna]

    print(matriz[linha])

print(f"O maior numero da matriz é: {maior}")




