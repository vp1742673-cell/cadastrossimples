#Apenas a tela de visualiçao 
while True:
    print(=============)
    print(sistema de cadastro)
    print(=============)

    print(1-cadastrar)
    print(2-fazer login)
    print(3-sair)

    opcao=int(input("escolha uma opcao"))
    #funcionalisdades
    #se o usario digitar o valor 1,vai ser exebido
    #a acao abaixo
    if(opcao==1):
        print("============")
        print("======tela de cadastro====")
        print("====================")
    elif(opcao==2):
        print("====================")
        print("===tela de login===")
        print("=====================")
    else:    
        print("voce esta saindo do cadastro,ate mais!")
        break