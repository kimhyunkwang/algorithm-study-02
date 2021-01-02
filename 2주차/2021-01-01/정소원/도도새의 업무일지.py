N, B = int(input()), list(map(int, input().split()))

diaryA, res = [], B[0]
for i in range(len(B)):
    if i > 0:
        res = B[i]*(i+1) - B[i-1]*i
    diaryA.append(str(res))
print(" ".join(diaryA))
