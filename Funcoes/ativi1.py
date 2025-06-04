lista = []

for i in range(5):
    numero = int(input(f"Digite o {i+1} numero:  "))
    lista.append(numero)

def soma_elementos (lista):
    sum(lista)
    return sum(lista)

print(f"Valores da lista original:{lista}")
print(f"O valor da soma dos elementos da lista é: {soma_elementos(lista)}")




    


