num, workhour = map(int, input().split())
work = []
for i in map(int, input().split()):
    work.append(i)
cnt = 0
ans = 0
for i in work:
    cnt += i
    if cnt >= workhour:
        break
    ans += 1

print(ans)