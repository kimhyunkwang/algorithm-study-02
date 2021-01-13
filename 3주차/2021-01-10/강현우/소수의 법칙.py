from math import sqrt

def prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1

N = int(input())

ans = 0

for i in range(N,2*N):
    if prime(i) == 1: 
        ans += 1

print(ans)
