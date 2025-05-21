print ("qual dos caminhos da floresta deseja seguir?")
print ("opcao A ira te direcionar para o rio")
print ("opcao B ira te direcionar para a montanha")

escolha1 = input("a ou b? ")

if escolha1 == "a":
    
    rio = input("voce chegou ao rio. Deseja atravessalo? s para SIM e n para NAO.   ")

    if rio == "s":
        print("voce conseguiu atravessar o rio!!")

    elif rio == "n":
        print ("voce preferiu nao atravessar o rio e voltou para floresta.")

    else:
        print("voce nao sabia qual decisao tomar.")

elif escolha1 == "b":

    montanha = input("voce conseguiu chegar a montanha. Deseja subir la? s para SIM e n para NAO.   ")

    if montanha == "s":
        print("voce conseguiu subir a montanha depois de muito enforco!!")

    elif montanha == "n":
        print("voce preferiu nao subir a montanha e voltar para a floresta.")

    else:
        print("voce ficou muito indeciso e com medo de subir a motanha.")



 













    





























