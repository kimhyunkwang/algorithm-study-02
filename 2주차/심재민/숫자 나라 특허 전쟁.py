# 숫자 나라 특허 전쟁

N = int(input())

three = []
five = []

for i in range(1, N):
    if i % 3 == 0:
        three.append(i) 
    elif i % 5 == 0:
        five.append(i) 
        
num = three + five 

print(sum(set(num))) 