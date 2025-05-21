import random 

letrasAlfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]

random.shuffle(letrasAlfabeto)

letra = random.choice(letrasAlfabeto)

escolha = int(input(f"Em qual posicao de 0 a 25 voce acha que esta {letra}?:    "))

decisao = letrasAlfabeto.index(letra)

if escolha == decisao:
    print("Voce acertou a posicao da letra!!")
else:
    print("Voce errou a posicao da letra!!")

