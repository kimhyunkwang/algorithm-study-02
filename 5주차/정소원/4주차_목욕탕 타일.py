# 단순..최대 공약수..문제..
import sys
import math
from copy import copy

A, B = 1, 1
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
G = math.gcd(n, m)
ans = (n//G)*(m//G)
# 일정한 크기의 타일을 붙이는 문제이므로,
# 해당 n, m를 최대로 채울 수 있는 정사각형 변의 크기는 = n,m 최대 공약수이다.
# 따라서, 각 정사각형 변만큼 각 변에 나누어준 수(=최대로 채우는 양)을 곱해주면 된다.
print(ans)


# 오답노트(틀린이유분석)
N, M = [int(input()) for _ in range(2)]


def getSquareNum(r, c):
    n, m = min(r, c), max(r, c)
    if n == 0:
        return 0
     # 가로, 세로 길이 중 더 작은 타일 크기의 정사각형을 최대로 채우고
     # 남은 부분에 대해서 재귀적으로 똑같이 처리하였다
     # 해당 경우는 일정한 정사각형을 구하는 문제가 아니었더라도 반례가 생기기도 하지만..!
     # 문제에서 요구한 것 자체가 가장 큰 정사각형으로 모두 채우는 경우(크기가 다른 정사각형없이)이므로 해당 경우는 당연히 틀린다.
     return m//n + getSquareNum(n, m%n)

print(getSquareNum(N, M))
