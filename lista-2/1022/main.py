import math


def mdc(a, b):
    return math.gcd(a, b)


def simplificar_fracao(n, d):
    divisor = mdc(abs(n), abs(d))
    n_simplificado = n // divisor
    d_simplificado = d // divisor
    return n_simplificado, d_simplificado


def resolver():
    try:
        n_casos = int(input())
    except EOFError:
        return
    except ValueError:
        return

    for _ in range(n_casos):
        try:
            linha = input().split()
        except EOFError:
            break

        if len(linha) < 7:
            continue

        n1 = int(linha[0])
        separador1 = linha[1]
        d1 = int(linha[2])
        operador = linha[3]
        n2 = int(linha[4])
        separador2 = linha[5]
        d2 = int(linha[6])

        n_resultado = 0
        d_resultado = 0

        if operador == '+':
            n_resultado = n1 * d2 + n2 * d1
            d_resultado = d1 * d2
        elif operador == '-':
            n_resultado = n1 * d2 - n2 * d1
            d_resultado = d1 * d2
        elif operador == '*':
            n_resultado = n1 * n2
            d_resultado = d1 * d2
        elif operador == '/':
            n_resultado = n1 * d2
            d_resultado = n2 * d1

        n_simplificado, d_simplificado = simplificar_fracao(
            n_resultado, d_resultado)

        if d_simplificado < 0:
            n_simplificado *= -1
            d_simplificado *= -1

        if d_resultado < 0:
            n_resultado_print = n_resultado * -1
            d_resultado_print = d_resultado * -1
        else:
            n_resultado_print = n_resultado
            d_resultado_print = d_resultado

        print(
            f'{n_resultado_print}/{d_resultado_print} = {n_simplificado}/{d_simplificado}')


resolver()
