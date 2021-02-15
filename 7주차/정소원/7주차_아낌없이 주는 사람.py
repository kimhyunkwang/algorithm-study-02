N = int(input())
gb = [-1] * (N + 1)
gb[1] = 1

for i in range(2, N + 1):
    if i % 2 == 0:
        gb[i] = (gb[i - 1] * 2 + 1) % 10007
    else:
        gb[i] = (gb[i - 1] * 2 - 1) % 10007
print(gb[N])