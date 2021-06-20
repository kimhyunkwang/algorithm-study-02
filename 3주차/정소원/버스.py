# 최소공배수
import math
A, B = map(int, input().split())

gcd = math.gcd(A, B)
print(A*B//gcd)