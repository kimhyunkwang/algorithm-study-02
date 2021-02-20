x, y, h = map(int, input().split())

dist = 2 * h
day = 0

while(True):
    if x + (x - y) * day >= dist: 
        break
    day += 1

print(day + 1)