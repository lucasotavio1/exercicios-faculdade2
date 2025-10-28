soma = cont = 0

while (True):
    try:
        nome = input()
        distancia = int(input())

        soma = soma + distancia
        cont = cont + 1

    except EOFError:
        if cont > 0:
            print(f'{soma / cont:.1f}')

        break
