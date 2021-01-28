string = input()

string = string.upper()
dict = {}

for s in string:
    if s in dict.keys():
        dict[s] += 1
    else:
        dict[s] = 1

count = 0
for key, value in dict.items():
    if value == max(dict.values()):
        count += 1
        ans = key

if count == 1:
    print(ans)
else:
    print("?")