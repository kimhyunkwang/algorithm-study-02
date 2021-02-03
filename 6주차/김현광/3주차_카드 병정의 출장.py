import itertools

n, m = map(int, input().split())
soldier_list = [i for i in range(1, n+1)]

case_list = list(itertools.combinations(soldier_list, m))

for case in case_list:
    for i in range(len(case)):
        print(case[i], end=" ")
    print("")