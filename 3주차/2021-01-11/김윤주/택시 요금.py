n = int(input())
d = list(map(int, input().split()))

sam = 0
gang = 0

for i in d:
    sam += (i//100+1)*100   #99m 마다 100원
    gang += (i//200+1)*180  #199m 마다 100원

if gang > sam:
    print("삼보운수", sam)
else:
    print("강남운수", gang)