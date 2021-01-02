# 덧셈을 모르는 체셔

N = int(input())

ans = 0

if len(str(N)) == 2:
    ans = int(str(N)[0]) + int(str(N)[1])
elif len(str(N)) == 3:
    if N % 10 == 0:
        ans = int(str(N)[0]) + int(str(N)[1:])
    else:
        ans = int(str(N)[:2]) + int(str(N)[2])
else:
    ans = 20
    
print(ans)