from math import sqrt as raiz
from faker import Faker
from random import uniform as gerar
import sys

fake = Faker('pt_BR')
for caminhos in sys.path:
    print(caminhos)
print()

dic_nomes = {}
teste_dic = {'Endereço': '', 'E-mail': '', 'Nota 1': 0, 'Nota 2': 0, 'Média': 0}
for pessoas in range(10):
    quant = 0
    lista = []
    lista = [fake.address(), fake.email(), f'{gerar(0.00, 10.00):.2f}', f'{gerar(0.00, 10.00):.2f}']
    lista.append(f'{raiz(float(lista[-1]) * float(lista[-2])):.2f}')
    for infs in teste_dic:
        teste_dic[infs] = lista[quant]
        quant += 1
    dic_nomes[fake.name()] = teste_dic


for nomes in dic_nomes:
    print(nomes)
    for infos in dic_nomes[nomes]:
        print(f'{infos}: {dic_nomes[nomes][infos]}')
    print()