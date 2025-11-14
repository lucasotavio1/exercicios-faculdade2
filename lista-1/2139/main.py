import datetime


natal = datetime.date(2016, 12, 25)

while True:
    try:
        mes, dia = map(int, input().split())

        data_informada = datetime.date(2016, mes, dia)

        if data_informada == natal:
            print('E natal!')
        elif data_informada == natal - datetime.timedelta(days=1):
            print('E vespera de natal!')
        elif data_informada > natal:
            print('Ja passou!')
        else:
            dias_faltando = (natal - data_informada).days
            print(f'Faltam {dias_faltando} dias para o natal!')

    except EOFError:
        break
