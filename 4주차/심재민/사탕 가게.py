# [구현] 사탕 가게

N = int(input())

candy = [N]

while N != 1:
    if N % 2 == 0:
        N = N // 2
        candy.append(N)
    else:
        N = (N * 3) + 1
        candy.append(N)

print(max(candy))