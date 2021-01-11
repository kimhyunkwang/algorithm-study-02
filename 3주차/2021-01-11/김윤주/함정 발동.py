o = ''
e = ''

for i in range(8):      #홀수줄 짝수줄별로 폭탄의 위치가 같으므로 나눠서 받아주기
    if i % 2 == 0:
        o += input()
    else:
        e += input()

a = 0

for i in range(len(o)):
    if i % 2 == 0 and o[i] == 'H':  #홀수줄에서 폭탄과 같은 위치에 H가 있을때
        a+=1

for i in range(len(e)):
    if i % 2 == 1 and e[i] == 'H':  #짝수줄의 경우
        a+=1

print(a)