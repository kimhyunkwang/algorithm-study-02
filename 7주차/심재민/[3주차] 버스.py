# [수학] 버스

A, B = map(int, input().split())

def LCM(A, B):
    
    if A > B:
        m = A
    else:
        m = B
    
    for i in range(m, A*B+1):
        if (i % A == 0) and (i % B == 0):
            res = i
            break
    
    return res

print(LCM(A, B))