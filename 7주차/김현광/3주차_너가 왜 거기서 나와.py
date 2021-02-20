n = input()

str_num = ''
i = 1

while(True):
    str_i = str(i)
    str_num += str_i

    if n in str_num[-len(n)-len(str_i):]:
        print(str_num.find(n) + 1)
        break

    i += 1