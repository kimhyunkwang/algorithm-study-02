# [BFS] 가로세로 숫자 퍼즐
# https://opentutorials.org/module/2980/17519 참고

from functools import reduce

def prod(t):
    return reduce(lambda x, y: x*y, t)

N = int(input())

sample = [list(map(int, input().split())) for _ in range(N)]

# [[16, 39, 5, 42, 96], [86, 56, 0, 48, 35], [19, 80, 81, 68, 5], [4, 52, 8, 83, 97], [88, 36, 68, 87, 16]]

result = []

for i in range(N-3):
    for j in range(N-3):
        result.append(prod([sample[i+k][j+k] for k in range(0,4)]))
        result.append(prod([sample[i+k][j+3-k] for k in range(0,4)]))

for i in range(N):
    for j in range(N-3):
        result.append(prod(sample[i][j:j+4]))
        
for i in range(N-3):
    for j in range(N):
        result.append(prod([sample[i+k][j] for k in range(0,4)]))

print(max(result))