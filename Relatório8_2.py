from time import sleep
def linha():
    print('-='*20)
vendas = []
media_vendas = 0
while True:
    print("\n--- Análise de Vendas ---")
    print("1. Adicionar venda")
    print("2. Visualizar vendas e estatísticas")
    print("3. Sair")

    opcao = input('Qual ação deseja tomar: ')
    if opcao == '1':
            add_vendas = float(input('Digite de quanto foi a sua venda: '))
            vendas.append(add_vendas)
            media_vendas += add_vendas
            continue
    elif opcao == '2':
            if len(vendas) < 1:
                print('Não há vendas registradas.')
                continue
            else:
                linha()
                print(f'Vendas: {vendas}')
                linha()
                print(f'A maior venda foi de {max(vendas)}.')
                print(f'E a menor venda foi de {min(vendas)}')
                print(f'E a média das vendas foi de: {(media_vendas / len(vendas)):.2f}')
                linha()
                sleep(1)
                continue
    elif opcao == '3':
        break
    else:
        print('Opção não reconhecida. Tente novamente...')
        continue