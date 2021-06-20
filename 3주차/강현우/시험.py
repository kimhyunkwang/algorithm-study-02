N = int(input())
answer = input()

blue = "54321" * 20
red = "12345" * 20
yellow = "3" * 100

color = {"red":0,"blue":0,"yellow":0}

for i in range(N):
    if blue[i] == answer[i]:
        color["blue"] += 1
    if red[i] == answer[i]:
        color["red"] += 1
    if yellow[i] == answer[i]:
        color["yellow"] += 1

color_items = list(color.items())
color_values = list(color.values())
max_value = max(color_values)
count = 0

for i in color_items:
    if i[-1] == max_value:
        count +=1

if count == 1:
    for i in color_items:
        if i[-1] == max_value:
            print(max_value)
            print(i[0])
else:
    print(max_value)
    for i in color_items:
        if i[-1] == max_value:
            print(i[0])