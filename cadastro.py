#variaveis para cadastro 
nome=""
idade=""
usuario=""
senha=""
#Apenas a tela de visualizacao
    while True:
    print("=========")
    print("sistema de cadastro")
    print("=========")

    print ("1-cadastrar")
    print("2-fazer login")
    print("3-sair")
    
    opcao= input("Escolha uma opcao:")
    #Funcionalidades
    #Se o usuario digitar o valor 1, vai ser exebido
    # a açao abaixo:
    if (opcao=="1"):
        print("============")
        print("======Tela de cadastro===")
        print ("========================")
        nome= input("Digite o seu nome")
        idade=input("Digite a sua idade:")
        usuario=input("Digite o seu usuario:")
        senha=input("Digite a sua senha:") 
        # se digitar2,abre a tela de login
        elif(opcao=="2"):
        print("===tela de login====") 
        print("==========")
        #se digitar3,sai da execucao  
        elif (opcao=="3"):
            print("voce esta saindo do cadastro,ate mais!")
            break
                                                            