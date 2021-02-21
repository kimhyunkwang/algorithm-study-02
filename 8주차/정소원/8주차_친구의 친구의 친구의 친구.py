# 인접행렬, 인접리스트, 간선리스트를 가지고 푸는 방식
# 트리의 지름을 활용한 dfs 풀이코드는 아래 참고
# https://kdt-gitlab.elice.io/yjk5309/algorithm-study-02/-/blob/master/7주차/정소원/7주차_친구의%20친구의%20친구의%20친구.py
N, M = map(int, input().split())

# 인접행렬, 간선리스트, 인접리스트
mtx = [[0] * N for _ in range(N)]
edges = []
adj = [[] * N for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    mtx[u][v] = 1
    mtx[v][u] = 1
    edges.append((u, v))
    adj[u].append(v)
    adj[v].append(u)


def findVertex(base, dep):
    for v in base:
        if v not in dep:
            return True
    return False


res = 0
for i in range(M - 1):
    a, b = edges[i]
    for j in range(i + 1, M):
        c, d = edges[j]
        vertex = [a, b, c, d]
        if len(set(vertex)) != 4:
            continue
        if mtx[a][c] == 1:
            # b, c 에 a,b,c,d 이외의 정점이 있으면 만족
            if findVertex(adj[b], vertex) or findVertex(adj[d], vertex):
                res = 1
                break
        if mtx[a][d] == 1:
            if findVertex(adj[b], vertex) or findVertex(adj[c], vertex):
                res = 1
                break
        if mtx[b][c] == 1:
            if findVertex(adj[a], vertex) or findVertex(adj[d], vertex):
                res = 1
                break
        if mtx[b][d] == 1:
            if findVertex(adj[a], vertex) or findVertex(adj[c], vertex):
                res = 1
                break

print(res)