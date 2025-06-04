print("Digite uma palavra qualquer a seguir.")

texto = input("Digite a palavra: ")

caractere = input("Digite o caractere que deseja contar: ")

def contar_caracteres(texto, caractere):
    contador = 0 
    for i in texto:
        if i == caractere:
            contador += 1 
    return contador

resultado = contar_caracteres(texto, caractere)

print(f"O caractere '{caractere}' apareceu {resultado} vezes na palavra '{texto}'.")