# 도도새의 업무일지

N = int(input()) 

b = [int(x) for x in input().split()] 

a = [] 

i = 0

while True:
    a.append((b[i] * (i+1)) - sum(a[:i]))
    i += 1
    if i == N:
        break

for i in range(N):
    print(a[i], end = ' ')