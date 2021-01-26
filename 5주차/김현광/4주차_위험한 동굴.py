from itertools import permutations

n = int(input())
people = [i+1 for i in range(n)]
cases = list(permutations(people, n))

for case in cases:
    for i in range(n):
        print(case[i], end = " ")
    print("")