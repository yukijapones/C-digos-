vetorPalavras = []

print("Digite 5 palavras a seguir.")

for i in range (5):
    palavra = input(f"Escreva a {i+1}ª palavra: ")
    vetorPalavras.append(palavra)

menor = vetorPalavras[0]
maior = vetorPalavras[0]

menorTamanho = 0
for letra in menor:
    menorTamanho += 1

for palavra in vetorPalavras:
    tamanho = 0
    for letra in palavra:
        tamanho += 1

    if tamanho < menorTamanho:
        menor = palavra
        menorTamanho = tamanho

    maiorTamanho = 0

    if tamanho > maiorTamanho:
        maior = palavra
        maiorTamanho = tamanho

print("Palavras digitadas:", vetorPalavras)
print(f"Menor palavra: {menor} ({menorTamanho} letras)")
print(f"Maior palavra: {maior} ({maiorTamanho} letras)")