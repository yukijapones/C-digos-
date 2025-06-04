print("Digite 5 numeros para o program dizer qual é o maior numero.")

lista = []

for i in range(5):
    numeros = input(f"Digite o {i+1} numero:     ")
    lista.append(numeros)

def maior_elemento (lista):
    max(lista)
    return max(lista)

print(lista)
print(f"O maior numero da lista dessa lista é: {maior_elemento(lista)}")