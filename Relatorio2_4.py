while True:
    print(str(bin(int(input('Digite um número para ter sua versão binária: '))))[2:])
    if str(input('Deseja continuar S/N: ')).lower()[0] == 'n':
        print('Até mais!')
        break