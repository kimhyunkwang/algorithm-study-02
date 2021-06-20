n = int(input())
distance = list(map(int, input().split()))

def sambo(n, d):
    total = 0
    for i in range(n):
        total += (d[i]//100 + 1) * 100
    return total

def gangnam(n, d):
    total = 0
    for i in range(n):
        total += (d[i]//200 + 1) * 180
    return total

sambo_price = sambo(n, distance)
gangnam_price = gangnam(n, distance)

if gangnam_price <= sambo_price:
    print("강남운수", gangnam_price)
else:
    print("삼보운수", sambo_price)