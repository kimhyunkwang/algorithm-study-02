x =input()
b = 0
r = 0

if x == ')(':          #“)(“ 의 경우 멸망이므로 분기
    print('NO')
else:
    for i in x:        #각 개수 더해주기
        if i == '(':
            b +=1
        else:
            r +=1

    if b == r :        #같을 경우만 성공
        print('YES')
    else:
        print('NO')