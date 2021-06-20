N, S = map(int, input().split())
plist = list(map(int, input().split()))

# 구간합
find = False
for size in range(1, N+1):
    start = 0
    while start+size <= len(plist):
        if sum(plist[start:start+size]) >= S:
            find = True
            break
        start += 1
    if find == True:
        break
if find == False:
    print(0)
else:
    print(size)
