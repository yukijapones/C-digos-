print ("Preencha as perguntas e coloque numeros inteiros.")

numero0 = float(input("digite o primeiro numero:  "))
numero1= float(input("digite o segundo numero:  "))
numero2 = float(input("digite o terceiro numero:  "))
numero3 = float(input("digite o quarto numero:  "))
numero4 = float(input("digite o quinto numero:  "))
numero5 = float(input("digite o sexto numero:  "))
numero6 = float(input("digite o setimo numero:  "))
numero7 = float(input("digite o oitavo numero:  "))
numero8 = float(input("digite o nono numero:  "))
numero9 = float(input("digite o decimo numero:  "))

numVetor = [numero0,numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8,numero9]

maior = numVetor[0]
menor = numVetor[0]

contador = 0

while contador < 10:
    if numVetor [contador] > maior:
        maior = numVetor[contador]
    if numVetor [contador] < menor:
        menor = numVetor[contador]

    contador += 1 

print ("O numero maior é:   ", maior)
print ("O numero menor é:   ", menor)

   

