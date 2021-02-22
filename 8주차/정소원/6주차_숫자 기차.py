# 백준 쉬운계단수와 같은 문제
# https://www.acmicpc.net/problem/10844

N = int(input())
mod = 1000000000
num = [[-1] * 10 for _ in range(N + 1)]
num[1] = [1 for i in range(10)]
num[1][0] = 0

for i in range(2, N + 1):  # i는 자릿수
    for j in range(10):
        if j == 0:  # j는 현재 문자(0-9)
            num[i][j] = num[i - 1][j + 1] % mod
        elif j == 9:
            num[i][j] = num[i - 1][j - 1] % mod
        else:
            num[i][j] = num[i - 1][j + 1] + num[i - 1][j - 1] % mod

print(sum(num[N]) % mod)