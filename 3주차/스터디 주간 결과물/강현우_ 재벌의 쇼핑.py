N,S = map(int, input().split())
product = list(map(int, input().split()))

product = sorted(product, reverse=True)
# print(product)
ans, s_copy = 0, S

ans1 = []
for i in range(N):
    ans, S = 0, s_copy
    for j in range(i,N):
        if S >= product[j]:
            S -= product[j]
            ans += 1
    if S > 0:
        ans = 0
    ans1.append(ans)

# print(ans1)
while 0 in ans1:
    ans1.remove(0)
# print(ans1)
    
try:
    print(min(ans1))
except:
    print(0)

# 제생각에는 맞게 짠것 같은데 40점 밖에 안나와서 혹시 어느부분이 문제 있는지 알려주시면 감사하겠습니다..!