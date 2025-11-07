from datetime import date
data_atual = date.today()

dia_nasc = int(input('Digite o dia de nascimento: '))
mes_nasc = int(input('Digite o mês de nascimento: '))
ano_nasc = int(input('Digite o ano de nascimento: '))

if data_atual.year - ano_nasc < 18:
    print('Negado menor de 18')
    exit()
elif data_atual.year - ano_nasc == 18:
    if data_atual.month >= mes_nasc and data_atual.day >= dia_nasc:
        print('Aprovado!! com 18')
    else:
        print('Reprovado!! mes ou dia')
        exit()
else:
    print('Aprovado!! com mais de 18')