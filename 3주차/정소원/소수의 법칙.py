# 소수는 1초과 sqrt(N)이하의 수에서 약수가 있는지의 여부만 탐색하면 된다. 
# [Reference] https: //ko.wikipedia.org/wiki/%EC%86%8C%EC%88%98_(%EC%88%98%EB%A1%A0)
import math
N = int(input())

def ckDecimal(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

res = 0
for i in range(N+1,2*N+1):
    if ckDecimal(i):
        res += 1

print(res)
