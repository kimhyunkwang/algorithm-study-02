n = int(input())
b = list(map(int, input().split()))
a = []
a.append(b[0])

for i in range(1,n):
    a.append(((i+1)*b[i])-(i*b[i-1]))
    
for i in (a):
    print(i, end=" ")