N = int(input())

result = ''
for i in range(1, N+1):
    result += str(i)

print(result.index(str(N))+1)