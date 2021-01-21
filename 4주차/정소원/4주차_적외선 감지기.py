A, B, C, D = map(int, input().split())
intruders = list(map(int, input().split()))


def getCaughtNum(n):
    res = 0
    x, y = n//(A+B), n//(C+D)
    xmn, ymn = (A+B)*x, (C+D)*y
    if n > xmn and n <= xmn+A:
        res += 1
    if n > ymn and n <= ymn+C:
        res += 1
    return res


for intruder in intruders:
    print(getCaughtNum(intruder))
