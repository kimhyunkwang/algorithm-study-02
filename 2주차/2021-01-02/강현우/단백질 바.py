want = int(input())
if want % 10 != 0:
    print(-1)
else:
    protein, chicube, peanut = 0,0,0
    while(want>=250):
        protein += 1
        want -= 250
    while(want>=40):
        chicube += 1
        want -= 40
    peanut = want // 10
    print(protein, chicube, peanut)