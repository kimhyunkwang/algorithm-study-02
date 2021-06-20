# [정렬] 별결 다 궁금해하네

N = int(input())

num = list(map(int, input().split()))

def sol(arr):

    sum_num = 0
    
    for i in range(N):
        
        for j in range(N):
            
            sum_num += abs(arr[i] - arr[j])
                
    return sum_num

print(sol(num))

# 채점 결과 시간 초과 오류로 80점 밖에 안나옵니다.
# 다른 방법이 있으면 알려주시면 좋을 것 같아요!