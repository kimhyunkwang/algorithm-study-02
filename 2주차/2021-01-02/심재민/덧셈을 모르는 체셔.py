# 덧셈을 모르는 체셔

# 자연수 A,B를 띄어쓰지 않고 하나의 수(N)으로 입력해준다.
# 앞에 있는 숫자를 A, 뒤에 있는 숫자를 B라고 가정한다.
N = int(input())

ans = 0 # initial value 설정

if len(str(N)) == 2: # N의 길이가 2이면, A와 B 모두 1자리 수 이므로 각각 더해준다.
    ans = int(str(N)[0]) + int(str(N)[1])
elif len(str(N)) == 3: # N의 길이가 3이면, A와 B 둘 중 하나는 10이다.
    if N % 10 == 0: # 이 때 N이 10으로 나누어 떨어지면, 뒤에 있는 숫자 B가 10이 된다.
        ans = int(str(N)[0]) + int(str(N)[1:])
    else: # N이 10으로 나누어 떨어지지 않으면, 앞에 있는 A가 10이 된다.
        ans = int(str(N)[:2]) + int(str(N)[2])
else: # N의 길이가 4이면, A와 B 모두 10이다.
    ans = 20
    
print(ans)