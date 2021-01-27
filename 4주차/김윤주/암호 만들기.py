n = int(input())

a = []

for i in range(n):
    a.append(input())
    
def c(s):
    answer = ''
    for i in s:
        if i == 'Z':                        #Z인 경우는 A를 반환
            answer += 'A'
        else:
            answer += str(chr(ord(i) + 1))  #i를 아스키코드로 바꾸고 1을 더해준 뒤 다시 문자열로 변환
    return answer


for i in a:
    print(c(i))