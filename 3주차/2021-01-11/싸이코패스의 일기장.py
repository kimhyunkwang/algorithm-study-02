# [정수론] 싸이코패스의 일기장

a = input()

l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = ''

for i in range(len(a)):
    for j in range(len(l)):
        if a[i] == l[j]:
            ans += l[j-4]
print(ans)