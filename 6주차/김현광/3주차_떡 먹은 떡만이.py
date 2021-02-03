m = int(input())

cur = 1

for i in range(m):
    change = list(map(int, input().split()))
    if cur in change:
        if cur != change[0]:
            cur = change[0]
        else:
            cur = change[1]

print(cur)