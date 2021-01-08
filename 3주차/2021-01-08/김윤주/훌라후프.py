import math

n = int(input())

r = list(map(int, input().split()))


def getNumOfLotation(a, b):
    gcd = math.gcd(a, b)       #math의 최대공약수 함수 사용
    A, B = a//gcd, b//gcd
    print(str(A)+"/"+str(B))


for i in range(1, n):
    getNumOfLotation(r[0], r[i])