# 단백질 바


N = int(input())


pure_protein = divmod(N, 250) 
chicken = divmod(pure_protein[1], 40) 
peanut = divmod(chicken[1], 10) 

if peanut[1] != 0: 
    print(-1)
else: 
    print(pure_protein[0], chicken[0], peanut[0])