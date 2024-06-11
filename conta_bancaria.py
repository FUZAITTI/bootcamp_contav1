menu = ""
conta = 0
limite_saque = 3
saques = 0
numero_de_saques = 1
historico = []




while True:
    menu = input("operação: ")
    if menu == "d":
        deposito = float(input("quanto depositar: "))
        if deposito <= 0:
            print("Deposito invalido: ")
        else :
            conta += deposito
            historico.append(f'Foi depositado R$ {deposito:.2f} na conta')
    




    elif menu == "e":
        for i in historico:
            print(i)
        print(f"Saldo da conta é: R$ {conta:.2f} ")    
    
    
    


    elif menu == "s":
        if numero_de_saques <= limite_saque:
            saques = float(input("Digite a quantidade a ser sacada: "))
            if saques > 0:
                if saques > 500:
                    print("Saques acima de R$ 500 não permitidos")
                else:    
                    if saques <= conta:
                        if saques > 500:
                            print("saque acima de R$ 500 não permitido")
                        else:
                            conta -= saques
                            historico.append(f'Foi sacado R$ {saques:.2f} da conta')
                            numero_de_saques += 1
                    else:
                        print("Salto insulficiente: ")
            else:
                print('Saque invalido')                        
        else:
            print("Limite de saques diarios ultrapassado")




    elif menu == "q":
        break



    else:
        print("Operação invalida")        
            

        


                    
