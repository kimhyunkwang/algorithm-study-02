from itertools import product

N, M = map(int,input().split())

N_list = list(range(1,N+1))

combi = list(product(N_list,repeat=M))

for i in range(len(combi)):
    print(' '.join(map(str, list(combi[i]))))