# 무어의 법칙[Moore’s Law]

# 기록할 N을 입력받는다.
N = int(input())

# 2에 N 제곱을 한 수를 string으로 변환해서 record 변수에 저장
record = str(2 ** N)

answer = 0 # initial value 설정

for i in record: # record에 있는 각 자릿 수의 숫자를 더해준다.
    answer += int(i)

print(answer)