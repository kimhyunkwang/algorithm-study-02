import math

N = int(input())

check = [False, False] + [True] * (2 * N)

for i in range(2, 2*N+1):
    if check[i]:
        for j in range(2*i, 2*N+1, i):
            check[j] = False

count = 0

for p in range(N, 2*N+1):
    if check[p]:
        count += 1
        
print(count)