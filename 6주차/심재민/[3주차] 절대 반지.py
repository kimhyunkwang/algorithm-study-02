hat_nick = input()
N = int(input())
M = [input().split() for _ in range(N)]

s = []
for i in range(N):
    s.append(M[i][0][-2]+M[i][0][-1]+M[i][0]+M[i][0][0]+M[i][0][1])

result = 0
for i in s:
    if hat_nick in i:
        result += 1

print(result)