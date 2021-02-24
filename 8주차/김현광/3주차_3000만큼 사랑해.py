N = input()

count = {}
keys = count.keys()

for c in N:
    if c not in keys:
        count[c] = 1
    else:
        count[c] += 1

if '6' in keys and '9' not in keys:
    x = count['6']
    del count['6']
elif '6' not in keys and '9' in keys:
    x = count['9']
    del count['9']
elif '6' in keys and '9' in keys:
    x = count['6'] + count['9']
    del count['6'], count['9']
else:
    x = 0

if x != len(N):
    maximum = max(count.values())
    if maximum >= x/2:
        print(maximum)
    else:
        if x % 2 == 0:
            print(x//2)
        else:
            print(x//2 + 1)
else:
    if x % 2 == 0:
        print(x//2)
    else:
        print(x//2 + 1)