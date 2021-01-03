n = int(input())
a =[]

for i in range(n):
    a.append(int(input()))
    
answer = str(sum(a))[:10]

print(answer)