D, K = map(int, input().split())
dc = [[-1] * 2 for _ in range(D + 1)]

dc[1], dc[2] = [1, 0], [0, 1]
for i in range(3, D + 1):
    dc[i] = [dc[i - 2][0] + dc[i - 1][0], dc[i - 2][1] + dc[i - 1][1]]

a, b = dc[D]
for i in range(a, K, a):
    for j in range(i + b, K + 1, b):
        if j == K:
            print(i // a, (j - i) // b, sep="\n")
            exit()