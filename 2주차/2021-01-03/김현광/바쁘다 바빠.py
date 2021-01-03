SUM = 0

for i in range(4):
    SUM += int(input())

minute = SUM // 60
second = SUM % 60

print(minute)
print(second)