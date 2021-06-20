jewel_before, jewel_after = {}, {}

for i in range(9):
    jewel_before[i] = 1
    jewel_after[i] = 1
jewel_before[6] = 2
jewel_after[6] = 2
ans = 1

N = input()

for i in N:
    if int(i) == 9:
        jewel_after[6] -= 1
    else:
        jewel_after[int(i)] -= 1
        
ans=[]

for i in range(len(jewel_after)):
    ans.append(list(jewel_before.values())[i] - list(jewel_after.values())[i])

if ans[6]/2 % 1 != 0:
    ans[6] = (ans[6]//2)+1
else:
    ans[6] = ans[6]//2

print(max(ans))