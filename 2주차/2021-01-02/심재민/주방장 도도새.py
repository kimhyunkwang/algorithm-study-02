# 주방장 도도새

# 들어온 주문의 수(N)과 도도새의 근무 시간(T)를 공백을 사용해서 
# 한 번에 입력받기
N, T = map(int, input().split())

# 각 주문을 처리하는 데 걸리는 시간을 주문 순서대로 공백을 사용해서 
# 한 번에 입력받고, list에 저장
order = [int(x) for x in input().split()]

sum_time = 0 # 각 주문을 처리하는데 걸리는 시간의 합

i = 0

while True:
    # order 리스트에 저장된 각 주문이 들어온 순서대로 걸리는 시간을
    # 첫 주문부터 1개씩 sum_time에 더해준다
    sum_time += order[i]
    i += 1
    # i 번째 주문까지 처리하는 시간(sum_time)이 도도새의 근무 시간(T)
    # 보다 크면 i-1을 출력하고 while문 탈출
    if sum_time > T: 
        print(i-1)
        break
    # 모든 주문을 처리했을 때, 주문을 처리한 총 시간이
    # 도도새의 근무 시간(T)보다 작으면 i를 출력하고 while문 탈출
    elif i == N:
        print(i)
        break