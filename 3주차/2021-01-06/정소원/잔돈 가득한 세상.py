N = int(input())

N = 10000-N
res, i = 0, 3
while i >= 0:
    res += N//10**i
    N = N % 10**i
    i -= 1
print(res)
