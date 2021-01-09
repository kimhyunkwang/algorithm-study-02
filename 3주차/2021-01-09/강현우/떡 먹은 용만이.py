M = int(input())

move = []

for i in range(M):
    move.append(list(map(int,input().split())))

youngman = 1

for i in move:
    if youngman in i:
        youngman = i[(i.index(youngman))-1]
        
print(youngman)