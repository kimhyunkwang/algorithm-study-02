new_number = ""
for i in range(1,100001):
    new_number += str(i)

N = input()

print((new_number.find(N))+1)