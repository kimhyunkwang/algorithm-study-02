from math import gcd

N = int(input())
M = int(input())

num = gcd(N,M)

print(int((N/num)*(M/num)))