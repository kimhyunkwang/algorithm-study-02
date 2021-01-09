N = int(input())
distance = list(map(int, input().split()))

sambo_dist, gangnam_dist = list(distance), list(distance)

for i in range(N):
    sambo_dist[i] = ((distance[i]//100)+1)*100
    if distance[i] % 200 < 100:
        gangnam_dist[i] = ((distance[i]//100)+2)*90
    else:
        gangnam_dist[i] = ((distance[i]//100)+1)*90
    
sambo = sum(sambo_dist)
gangnam = sum(gangnam_dist)

if sambo < gangnam:
    print(f"삼보운수 {sambo}")
else:
    print(f"강남운수 {gangnam}")