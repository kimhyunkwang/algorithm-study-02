n, m = map(int, input().split())
invalid = [[i] for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    invalid[a-1].append(b-1)
    invalid[b-1].append(a-1)


def dfs(v, l, ck, res):
    if l == 3:
        return res+1
    for i in range(n):
        if i <= v:
            continue
        if i not in ck:
            res = dfs(i, l+1, list(set(ck+invalid[i])), res)
    return res


count = 0
for i in range(n):
    count += dfs(i, 1, invalid[i], 0)
print(count)
