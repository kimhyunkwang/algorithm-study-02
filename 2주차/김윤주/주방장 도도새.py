n, worktime = map(int, input().split())
order = list(map(int, input().split()))
sum = 0
i = 0
while i < n:
    sum = sum + order[i]
    if sum > worktime:
        break
    else:
        i += 1
print(i)