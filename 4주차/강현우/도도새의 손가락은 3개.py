N = int(input())

num = [1,2,4]

for i in range(3, N):
    num.append((num[i-1]+num[i-2]+num[i-3])%123456)

print(num[N-1])