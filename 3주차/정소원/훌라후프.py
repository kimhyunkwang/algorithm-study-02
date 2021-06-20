import math

N = int(input())
radius = list(map(int, input().split()))


def getNumOfLotation(a, b):
    gcd = math.gcd(a, b)
    A, B = a//gcd, b//gcd
    print(str(A)+"/"+str(B))


for i in range(1, N):
    getNumOfLotation(radius[0], radius[i])
