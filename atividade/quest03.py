frase = input("Digite a frase:  ")
palavras = []
palaSeparadas = ""

for i in frase:
    if i != " ":
        palaSeparadas += i 
    else:
       if  palaSeparadas != "":
           palavras.append(palaSeparadas)
           palaSeparadas = ""

if palaSeparadas:
    palavras.append(palaSeparadas)

print (palavras)
        

           

        