from math import gcd

m, n = map(int,input().split())

if m == 0 and n == 0:
    print(0)
elif abs(m) + abs(n) <= 1:
    print(1)
elif gcd(m, n) == 1:
    print(1)
else:
    print(2)

# 집이 (5, 5)에 있다면 (1, 1)부터 (4, 4)까지 총 4개의 점이 가로막고 있지만
# (0,0) -> (2, 3) -> (5, 5) 방식으로 집이 어디에 있든 최대 2번만에 이동 가능하다.