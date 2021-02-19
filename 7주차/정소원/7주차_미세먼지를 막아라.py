# D(N) = D(n-1) + D(n-2)
N = int(input())
w = [-1] * (N + 1)
w[1], w[2] = 1, 2

for i in range(3, N + 1):
    w[i] = (w[i - 1] + w[i - 2]) % 10007
print(w[N])
