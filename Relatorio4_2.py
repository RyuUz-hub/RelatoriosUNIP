senha = 'senha123'
cont = 0
while cont < 3:
    if str(input('Digite sua senha: ')) != senha:
        print('SENHA INCORRETA!!!')
        cont += 1
        if cont == 3:
            print('Limite de tentativas alcançado. Tente novamente mais tarde!')
        continue
    
    print('Senha correta. Bem-vindo!!!')
    break