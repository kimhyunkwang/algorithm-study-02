years = list(map(lambda x: int(''.join(reversed(list(x)))), input().split()))

print(years[0]+years[1])
