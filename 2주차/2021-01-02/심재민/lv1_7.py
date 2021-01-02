# 김 박사의 비밀 데이터

N = int(input())

data = [int(input()) for _ in range(N)]

pwd = str(sum(data))

for i in range(10):
    print(pwd[i], end='')