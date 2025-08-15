usuarios = {
    "Gabriel": {"Senha":"123", "Saldo": 0.0},
    "Jordan": {"Senha":"456", "Saldo": 0.0},
    "Helder": {"Senha":"789", "Saldo": 0.0},
    "Joao": {"Senha":"987", "Saldo": 0.0},
    "Antonio": {"Senha":"654", "Saldo": 0.0}
    }
sistema = 0
while sistema == 0:
    print("Bem Vindo ao Sistema!\nInforme seu usuario para entrar!")
    menu = 0
    login = input("Usuario: ")
    senha = input("Senha: ")
    if login in usuarios and usuarios[login]["Senha"] == senha:
        print("Bem vindo, ",login)
        while menu == 0:
            print("O que deseja realziar no sistema? ")
            print(
                "1 - Consultar saldo\n" \
                "2 - Deposito\n" \
                "3 - Saque\n" \
                "4 - Transferencia\n" \
                "5 - Sair")
            escolha = int(input())
            if escolha == 1:
                print("Saldo atual: ",usuarios[login]["Saldo"])
            elif escolha == 2:
                deposito = float(input("Qual valor deseja depositar? "))
                print(deposito," depositados na conta")
                usuarios[login]["Saldo"] = usuarios[login]["Saldo"] + deposito
            elif escolha == 3:
                saque = float(input("Qual valor deseja sacar? "))
                if saque > usuarios[login]["Saldo"]:
                    print("Saldo insulficiente para a operação!")
                else:
                    usuarios[login]["Saldo"] = usuarios[login]["Saldo"] - saque
                    print(saque," sacados")
            elif escolha == 4:
                tranferencia = float(input("Digite o valor a ser tranferido: "))
                if tranferencia > usuarios[login]["Saldo"]:
                    print("Valor insulficiente na conta")
                else:
                    user_transfer = input("Para quem deseja tranferir? ")
                    if user_transfer in usuarios:
                        print(tranferencia,"foram tranferidos para ",user_transfer)
                        usuarios[login]["Saldo"] = usuarios[login]["Saldo"] - tranferencia
                        usuarios[user_transfer]["Saldo"] = usuarios[user_transfer]["Saldo"] + tranferencia
                    else:
                        print("Usuario não encontrado!")
            elif escolha == 5:
                menu = 1
            else:
                print("opção invalida")
                menu = 1
    else:
        print("Usuario não encontrado!")