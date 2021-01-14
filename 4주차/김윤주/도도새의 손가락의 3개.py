n = int(input())

list = [1,2,4]

for i in range(3, n):
    list.append(list[i-3]+list[i-2]+list[i-1])

answer = list[n-1] % 123456
print(answer)

#마지막 테스트케이스에서 시간초과