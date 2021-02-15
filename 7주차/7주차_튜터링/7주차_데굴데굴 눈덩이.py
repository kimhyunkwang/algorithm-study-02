import sys

N = int(input())
snow = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S = [[-1] * N for _ in range(N)]
distance = [[-1] * N for _ in range(N)]
mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def getDistance(x, y):
    if distance[x][y] != -1:
        return (S[x][y], distance[x][y])
    S[x][y], distance[x][y] = snow[x][y], 1
    for mx, my in mv:
        nx, ny = x + mx, y + my
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if snow[nx][ny] >= snow[x][y]:
                s, d = getDistance(nx, ny)
                if s + snow[x][y] >= S[x][y]:
                    S[x][y] = s + snow[x][y]
                    distance[x][y] = d + 1
    return (S[x][y], distance[x][y])


ms, md = -1, 0
for i in range(N):
    for j in range(N):
        s, d = getDistance(i, j)
        if s >= ms and d >= md:
            ms, md = s, d
print(md)
# Q. bfs로 분류되어 있어서, bfs로는 어떻게 푸는지 궁금합니다!(저는 dfs로 접근하였습니다.)

# [기타 건의사항] 제가 문제를 정확히 이해한건지는 모르겠지만 풀면서 개선했으면 좋겠는 점을 적어보았습니다..!

# 1. 해당 문제에서 이동횟수라고 표현을 하는데, 이동횟수에 처음 시작점도 포함된다는 표현이 들어가야 할 것 같습니다!

# 2. 해당 문제에서 최댓값이 나오는 경로가 여러개일 경우가 있는데
# 예를 들어 입력예시에서도 9->11->15(이동횟수:3), 4->5->11->15(이동횟수:4)
# 두 가지의 경우 눈덩이의 최댓값이 35로 같은데 답이 4인 것을 보아 눈덩이가 최댓값이고
# 이동 횟수가 최대인 값을 출력하라는 표현이 없어 애매하다고 생각합니다!
# 눈덩이의 최댓값이 여러개일때 최대 이동 횟수를 출력하라는 조건이 추가되어야하지 않을까요?
