from itertools import product

N, M = map(int,input().split())

N_list = list(range(1,N+1))

combi = list(product(N_list,repeat=M))

for i in combi:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()