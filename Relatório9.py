def adicionadados():
    dados = {'Telefone': input(f'Digite o telefone: '), 'Endereço': input(f'Digite o endereço: ')}
    return dados


def mostraitem(nome: str):
    if nome not in agenda:
        return print('Não localizado')
    print(f'Informações de {nome.capitalize()}:')
    for info in list(agenda[nome].keys()):
        print(f'{info.capitalize()}: {agenda[nome][info]}')

def adicionaitem(item: str):
    agenda['paulo'].setdefault(item, input(f'Digite a informação {item}: '))

#adicionaitem(str(input('Digite qual informação deseja adicionar: ')))

agenda = {}
while True:
    print("\n--- Menu da Agenda ---")
    print("1. Adicionar novo contato")
    print("2. Visualizar contato")
    print("3. Remover contato")
    print("4. Listar todos os contatos")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        agenda[input('Digite o nome do seu novo contato: ')] = adicionadados()
    if escolha == '2':
        contato = input('Qual contato deseja visualizar: ')
        if contato not in agenda:
            print('Contato não encontrado')
            continue
        print(f'\n{contato}:\nTelefone: {agenda[contato]['Telefone']}\nEndereço: {agenda[contato]['Endereço']}')
    if escolha == '3':
        try:
            agenda.pop(input('Digite qual contato deseja apagar: '))
        except KeyError:
            print('Nome não encontrado')
            continue
        print('Contato apagado')
    if escolha == '4':
        if len(agenda) == 0:
            print('Não possui contatos')
        for pessoas in agenda:
            print(f'\n{pessoas.upper()}:')
            for ks in agenda[pessoas]:
                print(f'{ks}: {agenda[pessoas][ks]}')