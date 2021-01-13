S = int(input())

ans = 0
for i in range(S+1):
    ans += i
    if ans > S:
        print(i-1)
        break
    elif ans == S:
        print(i)
        break