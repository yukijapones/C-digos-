text = input("Digite uma frase qualquer para saber a quantidade vogais que existem e quais sao:   ")

vogais = ""
quantidade = 0

for p in text:
    if p in ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" , "U" ]:
        vogais += p + ""
        quantidade += 1 
    


print ("As vogais presentes na frase sao:   ", vogais)
print ("A quantidade de vogais sao: ", quantidade)
    


