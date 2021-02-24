n = int(input())

square = 2 ** (n - 1)
remainder = 0

if (n == 1):
    print(1)
else:
    for i in range(n - 1):
        remainder += 2 ** i
    print(square + remainder/2)


## 틀린 풀이
## sqrt로 변의 길이를 구하면 부동소수점 오차로 인해 n이 48 이상이면 옳지 않은 값이 나온다.
from math import sqrt

n = int(input())

side = 1
area = []

for i in range(n):
    if i == 0:
        area.append(1)
    else:
        value = (side**2) * 0.75 + area[i-1]
        area.append(round(value, 1))

    side = side * sqrt(2)

print(area[-1])