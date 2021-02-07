hatter_nick = input()
n = int(input())
rings = []
for i in range(n):
    rings.append(input())

cnt = 0
for ring in rings:
    if ring.find(hatter_nick[0]) == -1:
        continue
    elif hatter_nick in ring:
        cnt += 1
    else:
        length = len(hatter_nick)
        for j in range(length - 1):
            x = -(j+1)
            y = length-j-1
            if ring[x:] + ring[:y] == hatter_nick:
                cnt += 1

print(cnt)