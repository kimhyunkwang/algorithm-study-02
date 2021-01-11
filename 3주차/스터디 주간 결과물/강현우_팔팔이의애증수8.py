L, R = map(int, input().split())

ans = 100

plus = 0

str_L, str_R = str(L), str(R)

for i in range(len(str_L)):
    if str_L[i] == 8 and str_R[i] == 8:
        str_L[i], str_R[i] = 0, 0
        plus += 1

L, R = int(str_L),int(str_R)

for i in range(L,R+1):
    i = str(i)
    cnt = i.count("8")
    if cnt < ans:
        ans = cnt
        
print(ans + plus)

# 시간초과가 2케이스에 대해서 떴는데 시간복잡도를 어떻게 줄일수 있는방법이 없을까 질문드려봅니다..!