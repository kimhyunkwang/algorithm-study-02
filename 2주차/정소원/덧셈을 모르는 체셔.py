num = input()

n1, n2 = '', ''
if len(num) == 2:
    n1, n2 = num[0], num[1]
elif len(num) == 3:
    if num[1] == '0':
        n1, n2 = num[:-1], num[2]
    else:
        n1, n2 = num[0], num[1:]
else:
    n1, n2 = num[0:2], num[2:]
print(int(n1)+int(n2))
