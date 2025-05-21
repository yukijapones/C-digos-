print ("Preencha as perguntas e coloque numeros inteiros.")

numero0 = int(input("digite o primeiro numero:  "))
numero1 = int(input("digite o segundo numero:  "))
numero2 = int(input("digite o terceiro numero:  "))
numero3 = int(input("digite o quarto numero:  "))
numero4 = int(input("digite o quinto numero:  "))
numero5 = int(input("digite o sexto numero:  "))
numero6 = int(input("digite o setimo numero:  "))
numero7 = int(input("digite o oitavo numero:  "))
numero8 = int(input("digite o nono numero:  "))
numero9 = int(input("digite o decimo numero:  "))

numVetor = [numero0,numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8,numero9]

print (numVetor)

maiorElementoVetor = numVetor[0]
posicaoVetor = 0

contador = 0

while contador < 10:

    if numVetor[contador] > maiorElementoVetor:

        maiorElementoVetor = numVetor[contador]
        posicaoVetor = contador

    contador += 1 

    
    
print ("O maior elemento dos vetores é: ", maiorElementoVetor)
print ("E a posicao dele é a:   ", posicaoVetor)
