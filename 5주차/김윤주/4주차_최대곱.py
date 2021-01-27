s, k = map(int, input().split())

remain = s%k
l = [s//k for i in range(k)]

for i in range(remain):
    l[i] += 1

ans = 1
for i in l:
    ans *= i
    
print(ans)

# 제일 크게 나뉘는 숫자를 구하고 나머지가 발생하면 +1을 해주고
# 그것들을 다 곱해준다