L, R = input().split()

if len(L) != len(R):
    print(0)
else:
    compare_len = len(L) - len(str(int(R) - int(L)))
    cnt_L, cnt_R = 0, 0
    for i in range(compare_len):
        if L[i] == '8':
            cnt_L += 1
        if R[i] == '8':
            cnt_R += 1
    print(min(cnt_L, cnt_R))