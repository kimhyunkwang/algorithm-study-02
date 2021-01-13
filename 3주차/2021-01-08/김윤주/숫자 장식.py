n, m = map(int, input().split())

number_list = [1 + i for i in range(n)]   # 숫자 리스트
check_number = [False] * n                # 중복숫자 체크
array = []                                # 출력할 수열
 
def DFS(x):
    if x == m:                            # 수열 m개를 충족할경우 출력
        print(*array)
        return
            
    for i in range(n):

        array.append(number_list[i])      # 수열 추가
        check_number[i] = True            # 사용한 수 체크

        DFS(x + 1)                        # + 1번째 수열을 위해 재귀함수 호출

        array.pop()                       # 수열 마지막 자리 삭제
        check_number[i] = False           # 사용한 수 초기화
DFS(0)

# from itertools import product

# N, M = map(int,input().split())

# N_list = list(range(1,N+1))

# combi = list(product(N_list,repeat=M)) 

# for i in range(len(combi)):
#     print(' '.join(map(str, list(combi[i])))) #튜플로 반환되기 때문에 list -> string 으로 바꿔 print
