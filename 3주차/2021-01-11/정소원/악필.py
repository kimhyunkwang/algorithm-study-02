# 최댓값은 7->9, 최솟값은 9->7
A, B = input().split()

def getMax(n):
    return int(''.join(map(lambda x: '9' if x=='7' else x, n)))

def getMin(n):
    return int(''.join(map(lambda x: '7' if x=='9' else x, n)))

print(getMax(A)+getMax(B), getMin(A)+getMin(B))