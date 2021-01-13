# 파이썬 내장함수 itertools를 이용한 풀이

from itertools import combinations

N, M = map(int, input().split())

list_N=list(range(1, N+1))


for i in combinations(list_N, M):
    print(*i)

# 백준 알고리즘 15650 (N과 M(2)) 풀이 참고

N, M = map(int, input().split())

check_number = [False] * N

arr = []

def combination(n, m, depth, idx):
    
    if depth == m:
        print(*arr)
        return
    
    for i in range(idx, N):
        
        if not check_number[i]:
            check_number[i] = True
            arr.append(i+1)
            
            combination(n, m, depth+1, i+1)
            
            check_number[i] = False
            arr.pop()

combination(N, M, 0, 0)