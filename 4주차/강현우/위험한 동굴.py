from itertools import permutations

N = int(input())
N_list = [i for i in range(1,N+1)]

permut = list(permutations(N_list,N))

for i in permut:
    for j in range(len(i)):
        print(i[j],end=" ")
    print()