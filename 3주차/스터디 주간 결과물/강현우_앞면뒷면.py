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

# 4번 케이스 까지 정답을 잘 나왔는데 마지막 케이스에서 
''' > (0/20) 프로그램에서 에러가 발생했습니다. 아래 에러메세지를 읽고 해결해 주세요.
.elice/runner.sh: line 1:    45 Killed                  python3 -u main.py '''
# 이런에러가 뜨고 점수조차 뜨지 않습니다 ㅠㅜ