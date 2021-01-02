a = input()
ans = 0
for i in a:
    if(i == "0"):
        ans += 9
    else:
        ans += int(i)
print(ans)
