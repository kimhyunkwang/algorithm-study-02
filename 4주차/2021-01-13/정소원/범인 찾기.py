N, K = map(int, input().split())

visited = [False for i in range(100001)]


def bfs(start, end):
    q, res = [(start, 0)], 100001
    visited[start] = True
    while len(q) > 0:
        cur, time = q.pop(0)
        # 만약 도둑이 있는 곳에 도착한 점이 있다면 그 중 최소시간을 대입
        if cur == end:
            res = min(time, res)
        # 다음 섹터의 후보가 되는 3개의 섹터
        nxt = [cur*3, cur-1, cur+1]
        # 다음 섹터를 queue에 넣기
        for v in nxt:
            # 섹터의 유효범위안에 있으며, 아직 방문하지 않은 섹터인 경우만 q에 넣기
            if (v >= 0 and v <= 100000) and not visited[v]:
                q.append((v, time+1))
                visited[v] = True
    return res


print(bfs(N, K))
