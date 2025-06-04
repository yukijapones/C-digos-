print("Digite uma palavra e descubra se ela e um palindromo ou nao.")

palavra = input("Digite aqui a palavra:  ")

def e_palindromo (palavra):
    palavra = palavra.lower()

    if palavra == palavra [::-1]:
        return True
    else:
        return False

resultado = e_palindromo(palavra)

if resultado:
    print(f"A palavra digitada {palavra} é um palindromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

    
   

