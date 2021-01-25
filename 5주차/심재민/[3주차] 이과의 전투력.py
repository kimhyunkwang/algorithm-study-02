N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
# [[55, 85], [58, 83], [88, 86], [60, 75], [46, 55]]

result = []
for i in range(N):
    result.append(1)

for i in range(N-1):
    for j in range(i+1, N):
        if (M[i][0] > M[j][0]):
            if (M[i][1] > M[j][1]):
                result[j] += 1
            else:
                continue
        elif (M[i][0] < M[j][0]):
            if (M[i][1] < M[j][1]):
                result[i] += 1
            else:
                continue
                
for i in range(len(result)):
    print(result[i], end = ' ')