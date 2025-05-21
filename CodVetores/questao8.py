print ("Insira as notas de cada aluno a seguir, e saiba a media da sala de aula.")

nota0 = float(input("Nota do 1 aluno:  "))
nota1 = float(input("Nota do 2 aluno:  "))
nota2 = float(input("Nota do 3 aluno:  "))
nota3 = float(input("Nota do 4 aluno:  "))
nota4 = float(input("Nota do 5 aluno:  "))
nota5 = float(input("Nota do 6 aluno:  "))
nota6 = float(input("Nota do 7 aluno:  "))
nota7 = float(input("Nota do 8 aluno:  "))
nota8 = float(input("Nota do 9 aluno:  "))
nota9 = float(input("Nota do 10 aluno:  "))
nota10 = float(input("Nota do 11 aluno:  "))
nota11 = float(input("Nota do 12 aluno:  "))
nota12 = float(input("Nota do 13 aluno:  "))
nota13 = float(input("Nota do 14 aluno:  "))
nota14 = float(input("Nota do 15 aluno:  "))

notasVetor = [nota0,nota1,nota2,nota3,nota4,nota5,nota6,nota7,nota8,nota9,nota10,nota11,nota12,nota13,nota14]

soma = 0
contador = 0 

while contador < 15:
    soma = soma + notasVetor[contador]
    contador = contador + 1 
media = soma / 15

print("A media da sala de aula é    ", media)
