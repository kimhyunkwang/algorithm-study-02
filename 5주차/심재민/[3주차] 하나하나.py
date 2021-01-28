s = input()

s = s.upper()

s = sorted(s)

count = {}

for i in s:
    try: count[i] += 1
    except: count[i]=1

result = [k for k, v in count.items() if max(count.values()) == v]

if len(result) == 1:
    print(*result)
else:
    print('?')