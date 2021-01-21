N = input()

sets, res = {}, 1

for ch in N:
    if ch in sets:
        sets[ch] += 1
    else:
        sets[ch] = 1

if '6' in sets and '9' in sets:
    if sets['6'] > sets['9']:
        sets['6'] -= sets['9']
    elif sets['9'] > sets['6']:
        sets['9'] -= sets['6']
elif '6' in sets:
    sets['6'] //= 2
    sets['9'] = sets['6']
elif '9' in sets:
    sets['9'] //= 2
    sets['6'] = sets['9']

print(max(sets.values()))
