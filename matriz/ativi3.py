matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

maiorNota = -1  
matriculaMaiorNota = -1  

for linha in range(5):
    matricula = int(input(f"Digite o número da matrícula do aluno {linha + 1}: "))
    
    
    matriz[linha][0] = matricula
    
    mediaProvas = int(input(f"Digite a média das provas do aluno {matricula}: "))
    mediaTrabalhos = int(input(f"Digite a média dos trabalhos do aluno {matricula}: "))
    
    
    matriz[linha][1] = mediaProvas
    
    matriz[linha][2] = mediaTrabalhos
    
    
    notaFinal = mediaProvas + mediaTrabalhos
   
    matriz[linha][3] = notaFinal
    
    if notaFinal > maiorNota:
        maiorNota = notaFinal
        matriculaMaiorNota = matricula


print("\nNotas finais dos alunos:")
for linha in matriz:
    print(f"Matrícula: {linha[0]}, Média das Provas: {linha[1]}, Média dos Trabalhos: {linha[2]}, Nota Final: {linha[3]}")

print(f"O aluno com a maior nota final foi o da matrícula {matriculaMaiorNota} com a nota final de {maiorNota}.")

    

