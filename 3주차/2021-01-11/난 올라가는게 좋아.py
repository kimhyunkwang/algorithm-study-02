# [정렬] 난 올라가는 게 좋아

N = int(input())

cord = [list(map(int, input().split())) for _ in range(N)]

def selection_sort(arr):
    
    for i in range(N-1):
        
        for j in range(i+1, N):
            
            if arr[i][1] > arr[j][1]:
                
                arr[i], arr[j] = arr[j], arr[i]
                
            elif arr[i][1] == arr[j][1]:
                
                if arr[i][0] > arr[j][0]:
                    
                    arr[i], arr[j] = arr[j], arr[i]
                    
    return arr

for x, y in selection_sort(cord):
    print(x, y)