N, M = map(int, input().split())


def combination(n, m, cur):
    if len(cur) == m:
        print(' '.join(cur))
        return
    for i in range(1, n+1):
        combination(n, m, cur+[str(i)])


combination(N, M, [])
