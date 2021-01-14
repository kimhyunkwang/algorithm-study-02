### 재귀
# test case 4, 5 실패
n = int(input())

def Recursion(n):
    if n == 1:
        return 1
    elif n  == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return Recursion(n-1) + Recursion(n-2) + Recursion(n-3)
    
print(Recursion(n) % 123456)


### DP
n = int(input())
data = []

for i in range(n):
    if i == 0:
        data.append(1)
    elif i == 1:
        data.append(2)
    elif i == 2:
        data.append(4)
    else:
        data.append(data[i-1] + data[i-2] + data[i-3] % 123456)

print(data[n-1])
