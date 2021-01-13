from math import gcd

num = int(input())
radius = list(map(int, input().split()))

for i in range(num-1):
    GCD = gcd(radius[0], radius[i+1])
    a = radius[0] // GCD
    b = radius[i+1] // GCD
    print(str(a) + "/" + str(b))