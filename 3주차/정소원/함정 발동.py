maze = [input() for i in range(8)]

res = 0
for i in range(8):
    for j in range(8):
        if maze[i][j] == 'H' and ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)):
            res += 1
print(res)
