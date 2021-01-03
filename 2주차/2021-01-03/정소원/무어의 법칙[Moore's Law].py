N = int(input())

rec, res = str(2**N), 0
for r in rec:
    res += int(r)
print(res)
