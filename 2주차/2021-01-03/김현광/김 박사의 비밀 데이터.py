n = int(input())
SUM = 0

for i in range(n):
    SUM += int(input())

password = str(SUM)[0:10]
print(password)