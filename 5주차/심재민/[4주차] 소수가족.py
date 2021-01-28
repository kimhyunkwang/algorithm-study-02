# [4주차] 소수가족

import math

a, b = map(int, input().split())
c = int(math.sqrt(b))
check = [False, False] + [True] * c

prime = 2

while prime * prime <= c:
    if not check[prime]:
        prime += 1
        continue
    for i in range(2*prime, c, prime):
        check[i] = False
    prime += 1

count = 0

for p in range(2,c):
    if not check[p]:
        continue
        
    mul = p*p
    while mul <= b:
        count += (a<= mul)
        mul *= p
        
print(count)