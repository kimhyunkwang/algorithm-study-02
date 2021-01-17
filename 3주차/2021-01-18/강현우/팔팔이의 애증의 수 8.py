L, R = map(str, input().split())

ans = 0

for i in range(len(L)):
    if L[i] == "8" and R[i] == "8":
        ans += 1
    else:
        break
        
print(ans)