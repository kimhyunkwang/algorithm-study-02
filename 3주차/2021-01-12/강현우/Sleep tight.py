X, Y, H = map(int, input().split())

ans = (2*H-X) / (X-Y)

if(ans%1 != 0):
    ans = int(ans) + 2
else:
    ans = int(ans) + 1 

print(ans)