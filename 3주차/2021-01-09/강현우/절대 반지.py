nickname = input()
num = int(input())
ring = []
for i in range(num):
    ring.append(input()*2)

ans = 0

for i in ring:
    if nickname in i:
        ans += 1

print(ans)