A, B = map(str, input().split())

back_ans_int = int(A[::-1]) + int(B[::-1])
back_ans_str = str(back_ans_int)
print(int(back_ans_str[::-1]))