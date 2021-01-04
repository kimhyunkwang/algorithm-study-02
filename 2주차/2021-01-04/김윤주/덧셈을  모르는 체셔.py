n = int(input())

if n < 100:
    answer = n // 10 + n % 10
elif n < 1000:
    if n % 10 == 0:
        answer = n // 100 + 10
    else:
        answer = 10 + n % 100
elif n == 1010:
    answer = 10 + 10

print(answer)