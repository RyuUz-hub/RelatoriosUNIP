from math import sqrt
from random import random, randint
from faker import Faker

fake = Faker('pt_BR')

print('Dados gerados aleatoriamente com Faker:\n')
print(f'Nome: {fake.name()}')
print(f'Email: {fake.email()}')
print(f'Endereço:\n{fake.address()}')
print(f'\n\nNotas geradas aleatoriamente com random:')
print(f'Nota 1: {randint(0, 9) + random():.2f}')
print(f'Nota 2: {randint(0, 9) + random():.2f}')