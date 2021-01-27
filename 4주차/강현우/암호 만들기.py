n = int(input())
password = []
for i in range(n):
    password.append(input())

answer = []

for i in password:
    part = ""
    for j in i:
        j = ord(j)
        j += 1
        if j > 90:
            j -= 26
        part += chr(j)
    answer.append(part)
    
for i in answer:
    print(i)