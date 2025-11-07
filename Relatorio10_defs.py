def menu():
    print('Escolha das opções abaixo:\n\n1 - Criar arquivo\n2 - Adicione conteúdo ao arquivo\n3 - Ler conteúdo do arquivo\n4 - Criptografar arquivo\n5 - Descriptografar conteúdo\n6 - Sair do programa')

def criar(arqv: str):
    conteudo = open(f'{arqv}.txt', 'w', encoding='utf-8')
    conteudo.close()

def adicionar(nome: str, cript=''):
    if cript != '':
        with open(f'{nome}.txt', 'w', encoding='utf-8') as arq:     
            arq.write(cript)  
            return
    with open(f'{nome}.txt', 'a', encoding='utf-8') as arq:
        quant = 0
        while True:
            quant += 1
            linha = input(f'O que deseja escrever na {quant}ª linha: ')
            if linha == 'parar':
                break
            arq.write(f'{linha}\n')

def ler(nome: str):
    with open(f'{nome}.txt', 'r', encoding='utf-8') as arq:
        texto = str(arq.read())
        return texto

def cripto(texto: str, chave: int):
    texto_criptografado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            start = ord('a')
        elif 'A' <= char <= 'Z':
            start = ord('A')
        else:
            texto_criptografado += char
            continue

        nova_posicao = (ord(char) - start + chave) % 26 + start
        texto_criptografado += chr(nova_posicao)
    return texto_criptografado