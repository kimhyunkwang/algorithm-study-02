day = int(input())
a = list(map(int, input().split()))
for i in range(len(a)):
    a[i] *= (i+1)
ans = []
ans.append(a[0])
for i in range(1, len(a)):
    ans.append(a[i]-a[i-1])
for i in (ans):
    print(i, end=" ")