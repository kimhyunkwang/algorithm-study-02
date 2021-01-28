A, B, C, D = map(int, input().split())
intruders = list(map(int, input().split()))


def getCaughtNum(n):
    res = 0
    x, y = n // (A + B), n // (C + D)
    xmn, ymn = (A + B) * x, (C + D) * y
    if n > xmn and n <= xmn + A:  # (A+B)로 나눈 최대의 몫(n)보다는 크고 (A+B)*n+A보다 작거나 같으면 걸린다.
        res += 1
    if n > ymn and n <= ymn + C:  # (C+D)로 나눈 최대의 몫(n)보다는 크고 (C+D)*n+B보다 작거나 같으면 걸린다.
        res += 1
    return res


# 따지고 보면 튜터님 코드와 같은 맥락이지만, 연산량이 더 많고 코드를 직관적으로 이해하기도 어렵다.
# 기존 코드에서 연산 부분 수정해보았다.(튜터님 코드는 비교 연산자를 덜 쓰려고 n-1을 해주신듯함)
# n을 (A+B), (C+D)로 나눈 나머지가 0초과-A이하, 0초과-B이하이면 감지기에 걸린다.


def getCaughtNum(n):
    res, x, y = 0, n % (A + B), n % (C + D)
    if x > 0 and x <= A:
        res += 1
    if y > 0 and y <= C:
        res += 1
    return res


for intruder in intruders:
    print(getCaughtNum(intruder))

# 튜터님 코드 추가


def FindAns(n):
    result = 0
    if (n - 1) % (A + B) < A:  # 0이상-A초미만 사이에 들어오면 X 적외선에 걸림
        result += 1

    if (n - 1) % (C + D) < C:  # 0초이상-C초미만 사이에 들어오면 Y 적외선에 걸림
        result += 1

    return result


A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

print(FindAns(P))
print(FindAns(M))
print(FindAns(N))
