from Relatorio10_defs import *

while True:
    menu()
    opcao = input("Escolha: ").strip()

    if opcao == '1':
        nome_arquivo_atual = input("Digite o nome do arquivo a ser criado: ")
        criar(nome_arquivo_atual)
    elif opcao == '2':
        if nome_arquivo_atual == "":
            print("Por favor, crie ou especifique um arquivo primeiro (Opção 1).")
            continue
        else:
            adicionar(nome_arquivo_atual)
    elif opcao == '3':
        if nome_arquivo_atual == "":
            print("Por favor, crie ou especifique um arquivo primeiro (Opção 1).")
            continue
        else:
            print(f'ARQUIVO:\n{ler(nome_arquivo_atual)}')
    elif opcao == '4':
        if nome_arquivo_atual == '':
            print("Por favor, crie ou especifique um arquivo primeiro (Opção 1).")
            continue
        else:
            criptografado = cripto(ler(nome_arquivo_atual), int(input('Digite a chave: ')))
            adicionar(f'{nome_arquivo_atual}', cript=criptografado)
    elif opcao == '5':
        descripto = cripto(ler(nome_arquivo_atual), 26 - int(input('Qual a chave usada para criptografar: ')))
        adicionar(nome_arquivo_atual, cript=descripto)
    elif opcao == '6':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")