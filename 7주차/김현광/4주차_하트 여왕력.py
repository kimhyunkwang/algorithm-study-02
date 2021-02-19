f, w, e = map(int, input().split())

i = 0

while(True):
    year = 15 * i + f
    if (year - w) % 28 == 0 and (year - e) % 19 == 0:
        break
    i += 1

print(year)

# year = 15 * x + f = 28 * y + w = 19 * z + e