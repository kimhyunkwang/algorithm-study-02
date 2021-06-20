bomb = 0

for i in range(8):
    line = input()
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and line[j] == "H":
            bomb += 1
        if i % 2 == 1 and j % 2 == 1 and line[j] == "H":
            bomb += 1
print(bomb)