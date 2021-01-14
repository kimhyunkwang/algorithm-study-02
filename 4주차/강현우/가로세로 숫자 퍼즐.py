N = int(input())
b = []

for i in range(N):
    b.append(list(map(int,input().split())))

# print(b)
ans = 0
for i in range(N-3):
    for j in range(N-3):
        diag1 = b[i][j]*b[i+1][j+1]*b[i+2][j+2]*b[i+3][j+3]
        if diag1 > ans:
            ans = diag1

for i in range(N-3):
    for j in range(N-3):
        diag2 = b[N-(i+1)][j]*b[N-(i+1)-1][j+1]*b[N-(i+1)-2][j+2]*b[N-(i+1)-3][j+3]
        if diag2 > ans:
            ans = diag2

for i in range(N-3):
    for j in range(N):
        vert = b[i][j]*b[i+1][j]*b[i+2][j]*b[i+3][j]
        if vert > ans:
            ans = vert
        
for i in range(N):
    for j in range(N-3):
        hori = b[i][j]*b[i][j+1]*b[i][j+2]*b[i][j+3]
        if hori > ans:
            ans = hori
print(ans)