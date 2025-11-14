n = int(input())
h = list(map(int, input().split()))

e_valido = 1

for i in range(1, n):
    if (h[i] > h[i-1] and (i % 2 == 0)) or (h[i] < h[i-1] and (i % 2 != 0)):
        e_valido = 0
        break

print(e_valido)
