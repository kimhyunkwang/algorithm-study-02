n = int(input())

ways = []

for i in range(n):
    if i == 0:
        ways.append(0)
    elif i == 1:
        ways.append(1)
    else:
        ways.append((ways[i-1] + ways[i-2]) * i)

print(ways[-1])


# n명의 카드 병정이 다음 해에 모두 새로운 무기를 사용할 수 있는 방법의 수는
# n = 1일 때, 0가지
# n = 2일 때, 1가지
# n = 3일 때, 2가지
# n = 4일 때, 9가지
# n = 5일 때, 44가지
# 규칙을 찾아서 점화식을 세우면 된다.