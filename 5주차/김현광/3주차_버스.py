from math import gcd

a, b = map(int, input().split())

def lcm(x, y):
    return int(x * y / gcd(x, y))

print(lcm(a, b))