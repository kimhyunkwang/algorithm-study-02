alphabet = {}

word = input().upper()

for i in word:
    alphabet[i] = 0
for i in word:
    alphabet[i] += 1

dic_items = list(alphabet.items())

dic_values = list(alphabet.values())
max_value = max(dic_values)

count = 0
for i in dic_items:
    if i[-1] == max_value:
        count +=1   

if count == 1:
    for i in dic_items:
        if i[-1] == max_value:
            print(i[0])
else:
    print("?")