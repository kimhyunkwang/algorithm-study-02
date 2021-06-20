n, k = map(int, input().split())
sum = 0

for i in range(1,n+1):
    sum = sum + i**k
    
answer = sum % 1000000009
print(answer)