A, B = map(str, input().split())

small_A, small_B = "", ""
for i in A:
    if i == '9':
        small_A += "7"
    else:
        small_A += i
for i in B:
    if i == '9':
        small_B += "7"
    else:
        small_B += i
small = int(small_A) + int(small_B)

big_A, big_B = "", ""
for i in A:
    if i == '7':
        big_A += "9"
    else:
        big_A += i
for i in B:
    if i == '7':
        big_B += "9"
    else:
        big_B += i
big = int(big_A) + int(big_B)

print(big, small)