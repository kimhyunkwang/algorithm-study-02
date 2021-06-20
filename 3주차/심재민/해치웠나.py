# [스택] 해치웠나...

s = input()

def defense(s):
    
    count_bomb = 0
    count_raser = 0
    ans = ''

    for i in s:
        if i == '(':
            count_bomb += 1
        elif i == ')':
            count_raser += 1
    
    if count_bomb == count_raser:
        ans = 'YES'
    else:
        ans = 'NO'
    
    return ans
    
print(defense(s))