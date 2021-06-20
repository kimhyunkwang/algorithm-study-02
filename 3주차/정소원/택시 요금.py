N, distance = int(input()), list(map(int, input().split()))

sambo, gangnam = 0, 0
for d in distance:
    sambo += (d//100+1)*100
    gangnam += (d//200+1)*180

if gangnam > sambo:
    print("삼보운수", sambo)
else:
    print("강남운수", gangnam)
