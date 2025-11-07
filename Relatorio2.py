consumo = 0

print('-'*33, '\nAlgoritmo para calcular o consumo\n' + '-'*33)
consumo = f'{(float(input('Digite a distância percorrida em km/h:\n')) / float(input('Digite o volume gasto de combustível:\n'))):.1f}'
print(f'Consumo médio: {consumo.replace('.', ',')}km/l')