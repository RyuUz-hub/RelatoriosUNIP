print('-'*15, '\nCalculando IMC:')
peso = (float(input('Digite seu peso em KG: ')) / ((float(input('Digite sua altura (em cm): '))/100)**2))
print(f'\nSeu IMC é de: {peso:.2f}')