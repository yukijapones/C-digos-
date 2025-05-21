vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
vistos = []
repetidos = []

for numero in vetor:
    if numero in vistos:
        if numero in repetidos:
            continue
        repetidos += [numero]
    else:
        vistos += [numero]

print("Números repetidos:", repetidos)