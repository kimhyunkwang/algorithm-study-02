n = int(input())
SUM = 0
n_str = str(2**n)

for i in range(len(n_str)):
    SUM += int(n_str[i])

print(SUM)