n = int(input())

list = [1,2,4]

for i in range(3, n):
    list.append((list[i-3]+list[i-2]+list[i-1]) % 123456)

answer = list[n-1]
print(answer)

#메모리 초과 오류 수정 완료