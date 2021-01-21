from itertools import permutations

N = int(input())

# 방법 1: permutations 함수 모듈 이용하기
p = permutations([str(i+1) for i in range(N)], N)
for line in p:
    print(' '.join(list(line)))


# 방법 2: dfs로 직접구현
def dfs(n, cur):
    if len(cur) == n:
        print(' '.join(list(map(lambda x: str(x), cur))))
        return
    for i in range(n):
        if i+1 not in cur:
            cur.append(i+1)
            dfs(n, cur)
            cur.pop()


res = dfs(N, [])
