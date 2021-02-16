import sys

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def vertical(x, y):
    if x + 3 <= n - 1:
        result = 1
        for i in range(4):
            result *= matrix[x][y]
            x += 1
        return result
    else:
        return 0

def horizontal(x, y):
    if y + 3 <= n - 1:
        result = 1
        for i in range(4):
            result *= matrix[x][y]
            y += 1
        return result
    else:
        return 0

def diagonal(x, y):
    if x + 3 <= n - 1 and y + 3 <= n - 1:
        result = 1
        for i in range(4):
            result *= matrix[x][y]
            x += 1
            y += 1
        return result
    else:
        return 0

def diagonal2(x, y):
    if x + 3 <= n - 1 and y - 3 <= n - 1:
        result = 1
        for i in range(4):
            result *= matrix[x][y]
            x += 1
            y -= 1
        return result
    else:
        return 0

ans_list = []

for i in range(n):
    for j in range(n):
        ans_list.append(vertical(i, j))
        ans_list.append(horizontal(i, j))
        ans_list.append(diagonal(i, j))
        ans_list.append(diagonal2(i, j))

print(max(ans_list))