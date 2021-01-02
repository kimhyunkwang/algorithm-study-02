num = int(input())
lst = []
for i in range(num):
    lst.append(int(input()))
ans = str(sum(lst))
print(ans[0:10])