from math import gcd

n = int(input())
m = int(input())

nq = n // gcd(n, m)
mq = m // gcd(n, m)
ans = nq * mq

print(ans)