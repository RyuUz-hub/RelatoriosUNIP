from time import sleep
def linha():
    print('-='*20)

tarefas = []
while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        adicao = input('Digite a tarefa que deseja adicionar: ')
        tarefas.append(adicao)
    elif escolha == '2':
        if len(tarefas) < 1:
            linha()
            sleep(1)
            print('Não há tarefas ainda...')
            sleep(0)
            linha()
            continue
        else:
            linha()
            for i in range(len(tarefas)):
                sleep(0.3)
                print(tarefas[i])
            linha()
            sleep(1)
            continue
    elif escolha == '3':
        exclusao = input('Qual tarefa deseja excluir: ')
        if tarefas.count(exclusao) < 1:
            linha()
            sleep(1)
            print('Tarefa não encontrada.')
            print('Verifique as tarefas e tente novamente.')
            sleep(0)
            linha()
            continue
        else:
            tarefas.remove(exclusao)
            linha()
            print(f'Tarefa "{exclusao}" removida')
            linha()
            sleep(1)
            continue
    elif escolha == '4':
             print("Saindo do gerenciador de tarefas. Até mais!")
             break
    else:
             print("Opção inválida. Por favor, tente novamente.")