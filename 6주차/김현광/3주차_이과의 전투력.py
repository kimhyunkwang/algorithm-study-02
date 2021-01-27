n = int(input())
scores = []
for i in range(n):
    scores.append(list(map(int, input().split())))
result = [1 for i in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if scores[i][0] > scores[j][0]:
            if scores[i][1] > scores[j][1]:
                result[j] += 1
        elif scores[i][0] < scores[j][0]:
            if scores[i][1] < scores[j][1]:
                    result[i] += 1

for i in range(n):
    print(result[i], end=" ")