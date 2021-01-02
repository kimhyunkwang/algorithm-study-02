num = int(input())
ans = 0
for i in range(1, num):
    if(i%3==0 or i%5==0):
        ans += i
print(ans)