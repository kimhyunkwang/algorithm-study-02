name = input()
n = int(input())

a=[]
for i in range(n):
    a.append(input())

answer = 0

for i in a:
    if name in i*2:      #반지가 이어지는 곳을 i*2로 표현
        answer+=1        #name이 포함되면 answer에 1 add

print(answer)