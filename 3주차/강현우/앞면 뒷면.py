# 내풀이
def yaksu(num):
    yaks = []
    for a in range(1, num+1): 
        if num % a == 0:
            yaks.append(a)
    return yaks

N = int(input())
dic = {}

for i in range(1,N+1):
    dic[i] = 0

for i in range(1,N+1):
    for j in yaksu(i):
        dic[i] += 1
ans =0
dic_values = list(dic.values())
for i in dic_values:
    if i % 2 == 1:
        ans += 1     
print(ans)

# 정소원님 풀이
# 대박 사건... 생각의 전환 Respect...

from math import sqrt

N = int(input())

print(int(sqrt(N)))
