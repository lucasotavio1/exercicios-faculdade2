while True:

    try:
        n, m = input().split()
        n = int(n)
        m = int(m)

        indexes = {}

        i = 0

        for aux in list(input().split()):
            try:
                indexes[int(aux) - 1].append(int(i))

            except:
                indexes[int(aux) - 1] = [int(i)]

            i += 1

        for i in range(m):
            k, v = input().split()
            k = int(k)
            v = int(v)

            try:
                print(indexes[v-1][k-1] + 1)

            except:
                print(0)

    except EOFError:
        break
