N = int(input())

b= [N]

while N != 1:
    if N % 2 == 0:
        N = N // 2
        b.append(N)
    else:
        N = 3*N +1
        b.append(N)

print(max(b))
