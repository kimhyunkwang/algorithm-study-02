# 정답코드(튜터님 코드 참고)
import math

A, B = map(int, input().split())

# 미리 소수 구하기 => 최대 경우의 수가 10**14이기 때문에,
# 최대 소수가족수를 만들수 있는 후보가 되는 값은 10**7 이하의 소수이다.
# `에라토스테네스의 체`의 원리를 이용하면 빠르게 모든 수에 대한 소수판별을 할 수 있다.
MAX = 10 ** 7
prime = [True] * (MAX + 1)
prime[0], prime[1] = False, False

i = 2
while i <= math.sqrt(MAX):
    if not prime[i]:
        i += 1
        continue
    for j in range(i * 2, MAX + 1, i):
        prime[j] = False
    i += 1

# A-B 사이 소수가족 수 구하기
res = 0
for n in range(2, MAX + 1):  # 최대 수
    if not prime[n]:  # 해당 수가 소수가 아니라면
        continue
    mul = n * n
    while mul <= B:
        res += A <= mul  # 조건문의 결과 True = 1, False = 0으로 카운팅 된다.
        mul *= n
print(res)

# 오답노트(틀린 이유 분석)
# 시간초과(60)
# 매 턴마다 소수인 값과 아닌 값을 미리 계산해두었어야 하는데
# 소수인 수에만 초점을 맞추어서 소수가 아닌 수에 대한 prime 계산을 계속 진행해서 시간초과가 발생하였다.
# 또한 반복문의 매턴마다 제곱연산이 계속 발생하고 있으므로, 해당 함수들에 대한 메모리 사용량이 증가하고 처리시간도 많이 발생한다.
import math


def prime(n):
    if n == 1:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


MAX = 10 ** 7 + 1
primes = [True] * MAX
primes[0], primes[1] = False, False


def countDemicalFamily(a, b):
    res, k, n = 0, 2, int(b ** 0.5)
    while b ** (1 / k) >= 2:
        k += 1
    while k >= 2:
        l, r = math.ceil(a ** (1 / k)), int(b ** (1 / k))
        for v in range(l, r + 1):
            if not primes[v]:
                continue
            if not prime(v):
                primes[v] = False
                for i in range(v + v, n + 1, v):
                    primes[i] = False
                continue
            res += 1
        k -= 1
    return res


A, B = map(int, input().split())
print(countDemicalFamily(A, B))
