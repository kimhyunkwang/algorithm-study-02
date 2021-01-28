# 백준 토마토 문제랑 똑같음
# https://www.acmicpc.net/problem/7576
import sys
from collections import deque

m, n = map(int, input().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
starts = [(y, x) for x in range(m) for y in range(n) if box[y][x] == 1]
mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 아래, 위, 오른쪽, 왼쪽


def ck_is_finished(box):
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return False
    return True


def bfs(starts, box):
    mnday = -1
    q = deque()  # 연산속도가 더 빠른 deque를 queue로 사용
    for y, x in starts:
        q.append((y, x, 0))  # 쥐의 (y좌료, x좌표, 지난 날짜수)를 큐에 넣기
    while len(q) > 0:
        y, x, d = q.popleft()
        for i in range(4):
            ny, nx = y + mv[i][0], x + mv[i][1]  # 감염시킬 생쥐의 좌표 탐색
            if ny < n and ny >= 0 and nx < m and nx >= 0 and box[ny][nx] == 0:
                box[ny][nx] = 1  # 감염 표시
                q.append((ny, nx, d + 1))  # 다음날 감염 여부를 파악하기 위해 해당 쥐의 좌표 q에 넣기
        if ck_is_finished(box):  # 만약 모든 생쥐가 감염되었다면 break
            mnday = d + 1
            break
    print(mnday)


if ck_is_finished(box):
    print(0)
else:
    bfs(starts, box)
