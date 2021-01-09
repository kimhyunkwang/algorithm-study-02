from itertools import combinations

N, M = map(int,input().split())

N_list = list(range(1,N+1))

combi = list(combinations(N_list,M))

for i in range(len(combi)):
    print(' '.join(map(str, list(combi[i]))))
