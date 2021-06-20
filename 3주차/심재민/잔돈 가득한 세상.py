# [그리디] 잔돈 가득한 세상

N = int(input())

change = 10000 - N

a = divmod(change, 1000)
b = divmod(a[1], 100)
c = divmod(b[1], 10)
d = divmod(c[1], 1)

ans = a[0] + b[0] + c[0] + d[0]

print(ans)