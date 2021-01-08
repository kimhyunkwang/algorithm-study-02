N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
strongers = [1 for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if scores[i][0] > scores[j][0] and scores[i][1] > scores[j][1]:
            strongers[j] += 1
        elif scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
            strongers[i] += 1
print(' '.join(map(lambda x: str(x), strongers)))
