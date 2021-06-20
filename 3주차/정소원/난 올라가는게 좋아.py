N = int(input())
vertex = [tuple(map(int, input().split())) for _ in range(N)]

res = sorted(vertex, key=lambda x: (x[1],x[0]))
for i in range(N):
    print(res[i][0], res[i][1])