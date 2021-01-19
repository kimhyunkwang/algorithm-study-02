# [수학] 최대 곱

S, K = map(int, input().split())

result = 1

def maxproduct(a, b):
    
    quote = a // b
    res = a % b
    elements = []
    
    while b > 0:
        if res > 0:
            elements.append(quote+1)
            res -= 1
        else:
            elements.append(quote)
        b -= 1
    
    return elements

for i in maxproduct(S,K):
    result *= i

print(result)