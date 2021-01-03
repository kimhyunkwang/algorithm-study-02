N = int(input())

pt, ck, pn = N//250, N % 250//40, N % 250 % 40//10
if N % 250 % 40 % 10 != 0:
    print(-1)
else:
    print(pt, ck, pn)
