odd, even = "",""

for i in range(1,9):
    if i % 2 ==1: #홀수번째 줄
        odd += input()
    else: #짝수번째 줄
        even += input()

ans = 0

for i in range(len(odd)):
    if i % 2 == 0:
        if odd[i] == "H":
            ans += 1
            
for i in range(len(even)):
    if i % 2 == 1:
        if even[i] == "H":
            ans += 1
        
print(ans)