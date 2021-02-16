# [DFS] 비타민 중독자

n, m = map(int, input().split())

vita = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    vita[j][i] = 1
    vita[i][j] = 1

# print(vita)

cnt = 0

for i in range(1,n+1):
    for j in range(i+1,n+1):
        if vita[i][j] == 0:
            for k in range(j+1,n+1):
                if (vita[i][k] == 0) and (vita[j][k] == 0):
                    # print(i, j, k)
                    cnt += 1

print(cnt)