from math import sqrt

n = int(input())

side = 1
area = []

for i in range(n):
    if i == 0:
        area.append(1)
    else:
        value = (side ** 2) * 0.75 + area[i - 1]
        area.append(round(value, 1))

    side = side * sqrt(2)

print(area[-1])


# test case 5번에서 오답이 나오는데 이유를 모르겠습니다!
# side를 출력해봤더니 정수 2가 2.0000000000000004 이런 식으로 나오는데 그래서 오답이 나오는 걸까요?
