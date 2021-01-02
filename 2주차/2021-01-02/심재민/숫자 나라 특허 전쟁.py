# 숫자 나라 특허 전쟁

# 자연수 N을 입력한다.
N = int(input())

three = []
five = []

for i in range(1, N):
    if i % 3 == 0:
        three.append(i) # N까지의 숫자 중에 3으로 나누어 떨어지는 숫자를 three list에 추가
    elif i % 5 == 0:
        five.append(i) # N까지의 숫자 중에 5로 나누어 떨어지는 숫자를 five list에 추가
        
num = three + five # 각 숫자 리스트를 num list에 모은다.

print(sum(set(num))) # 모아준 num list에 있는 중복된 숫자를 없애기 위해 set을 사용한 뒤 더해준다.