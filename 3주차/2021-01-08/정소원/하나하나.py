s = (input()).upper()

alpha = {}
for i in range(len(s)):
    if not s[i] in alpha:
        alpha[s[i]] = 1
    else:
        alpha[s[i]] += 1
alpha = sorted(alpha.items(), key=(lambda x: x[1]), reverse=True)

if len(alpha) > 1 and alpha[0][1] == alpha[1][1]:
    print('?')
else:
    print(alpha[0][0])
