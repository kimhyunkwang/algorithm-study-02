a, b = input().split()

def get_reverse(string):
    str_list = []
    for i in range(len(string)):
        str_list.append(string[i])

    str_list.reverse()

    while(str_list[0] == '0'):
        str_list.remove('0')

    result = ''
    for i in range(len(str_list)):
        result += str_list[i]

    return result

c = str(int(get_reverse(a)) + int(get_reverse(b)))
print(get_reverse(c))