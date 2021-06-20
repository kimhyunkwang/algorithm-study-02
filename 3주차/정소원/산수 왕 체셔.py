# 수식 참고 : https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation
# 분할정복으로 풀지 않고 DP로 해결함
import math

A, B, C = map(int, input().split())
res, cache = 0, [-1 for i in range(32)] # 최대 31회(2^31)

# binary로 바꾸어서 계산
def getBinarySum(n):
    b = bin(n)[:1:-1]
    res = []
    for i in range(len(b)):
        if b[i] == '1':
            res.append(2**i)
    return res

# A^2%C = (A%C*A%C)%C
# bottom -> top방식(아마도...)
def getBinaryMod(a, b, c):
    if cache[b] != -1:
        return cache[b]
    cache[b] = (getBinaryMod(a, b-1, c)**2)%c
    return cache[b]

res, cache[0], = 1, A%C
for val in getBinarySum(B):
    idx = int(math.log(val, 2))
    res *= getBinaryMod(A, idx, C)
print(res%C)
