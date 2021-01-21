### DP
n = int(input())
fibo = []
for i in range(n):
    if i == 0 or i == 1:
        fibo.append(1)
    else:
        fibo.append(fibo[i-1] + fibo[i-2])
print(fibo[n-1])


### 재귀
# test case 2, 4, 5 실패
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))