password = input()
answer = ""

for i in password:
    i = ord(i)
    i -= 4
    if i > 90:
        i -= 26
    elif i < 65:
        i += 26
    answer += chr(i)
    
print(answer)
