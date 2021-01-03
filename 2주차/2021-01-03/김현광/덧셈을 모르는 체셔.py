x = int(input())

if x < 100:
    answer = x // 10 + x % 10
elif x < 1000:
    if x % 100 // 10 == 0:
        answer = 10 + x % 100 % 10
    else:
        answer = x // 100 + 10
else:
    answer = 10 + 10

print(answer)