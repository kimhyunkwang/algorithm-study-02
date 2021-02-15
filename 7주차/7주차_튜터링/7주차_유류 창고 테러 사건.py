import sys
from copy import deepcopy
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
container, fire = [], []

for i in range(N):
    cur = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if cur[j] == 2:
            fire.append((i, j))
    container.append(cur)


def ckFire(container):
    for i in range(N):
        for j in range(N):
            if container[i][j] == 0:
                return False
    return True


def bfs(cur, container):
    q = deque()
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x, y in cur:
        q.append((x, y, 0))
        container[x][y] = 3  # 불이 붙은 곳은 3으로 표시

    while len(q) > 0:
        x, y, t = q.popleft()
        if ckFire(container):
            return t
        for mx, my in mv:
            nx, ny = x + mx, y + my
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if container[nx][ny] == 0:
                    container[nx][ny] = 3
                    q.append((nx, ny, t + 1))
    return t if ckFire(container) else -1


com = list(combinations(fire, M))
MAX = 999999999
res = MAX

for cur in com:
    box = deepcopy(container)
    ct = bfs(cur, box)
    if ct != -1:
        res = min(res, ct)

if res == MAX:
    print(-1)
else:
    print(res)

# Q. 문제에서 불이 빈칸으로 퍼진다고 했는데, 그럼 순수하게 값이 '0'인 곳으로만 불이 퍼질 수 있는 건가요?(가연성 물질이 있는 '2'로도 퍼질 수 있는 것인지)
# Q. 문제에서 2, 5번 테스트 케이스가 틀리는데, 어떤 부분에서 틀린것인지 잘 모르겠습니다...!
# (코드가 넘 길어서..정답 코드 첨부해주시면 설명 해주신 내용 위주로 보고 틀린 부분 스스로 찾아보겠습니다!)