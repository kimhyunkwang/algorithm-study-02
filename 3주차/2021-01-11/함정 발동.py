# [탐색] 함정 발동

status = [input().split() for _ in range(8)]

def trap(status):

    count = 0
    
    for i in range(8):
        
        if i % 2 == 0: # 홀수 행
            
            for j in range(8):
            
                if j % 2 == 0: # 홀수 번째
                    
                    if status[i][0][j] == 'H':
                        
                        count += 1

        else: # 짝수 행
        
            for k in range(8):
                
                if k % 2 == 1: # 짝수 번째
                
                    if status[i][0][k] == 'H':
                    
                        count += 1
                        
    return count

print(trap(status))