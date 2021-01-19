N = int(input())

mx = N
while N != 1:
    if N % 2 == 0:
        N //= 2
    else:
        N = N*3+1
    mx = max(mx, N)
print(mx)
