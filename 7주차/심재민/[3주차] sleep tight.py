X, Y, H = map(int, input().split())

a = 2 * H

total = 0

day = 0

while True:
    total += X
    day += 1
    if total >= a:
        break
    total -= Y

print(day)