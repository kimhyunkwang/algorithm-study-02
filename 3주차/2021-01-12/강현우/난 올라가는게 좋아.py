N = int(input())
loc = []
for i in range(N):
    loc.append(list(map(int,input().split())))

loc = sorted(loc, key=lambda x: (x[1],x[0]))

for i in range(N):
    print(loc[i][0], loc[i][1])