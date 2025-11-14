n, s = map(int, input().split())
saldo = s
menor_saldo = saldo

for _ in range(n):
    movimentacao = int(input())
    saldo += movimentacao
    menor_saldo = min(menor_saldo, saldo)

print(menor_saldo)
