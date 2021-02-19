n = int(input())

cnt = 0
i = 1
while(True):
    square_num = i**2
    if square_num <= n:
        cnt += 1
        i += 1
    else:
        break

print(cnt)