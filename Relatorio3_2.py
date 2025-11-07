lados = []
for i in range(3):
    lados.append(int(input('Digite um lado do seu triângulo: ')))
quant = 0
for i in range(3):
    if lados[quant] > (lados[quant - 2] + lados[quant - 1]):
        print('Não é um triângulo válido!!!')
        exit()
    quant += 1

if lados[0] == lados[1] == lados[2]:
    print('Você tem um triângulo euilátero!!!')
    exit()
if lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
    print('Você tem um triângulo isósceles!!!')
if lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
    print('Você tem um triângulo escaleno!!!')