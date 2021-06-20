M = int(input())
dduckman = [1, 2, 3]

for i in range(M):
    x, y = map(int, input().split())
    dduckman[x-1], dduckman[y-1] = dduckman[y-1], dduckman[x-1]

print(dduckman.index(1)+1)
