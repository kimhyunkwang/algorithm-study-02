N = int(input())
cache = [-1] * (N + 1)
cache[0], cache[1] = 0, 1

for i in range(2, N + 1):
    if i % 2 == 0:
        cache[i] = cache[i - 1] * 2 + 1
    else:
        cache[i] = cache[i - 1] * 2 - 1
print(cache[N])