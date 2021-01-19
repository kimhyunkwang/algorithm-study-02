F, W, E = map(int, input().split())

# 경우의 수: 7980
mx = 15*28*19
for i in range(286):
    n = 28*i+W
    if n % 15 == F % 15 and n % 19 == E % 19:
        print(n)
        break
