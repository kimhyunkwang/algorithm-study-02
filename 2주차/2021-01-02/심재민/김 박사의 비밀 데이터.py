# 김 박사의 비밀 데이터

# 김 박사가 저장할 데이터의 수를 입력받기
N = int(input())

# 입력받은 데이터 수(N) 만큼 40자리 숫자의 데이터를 한 줄 씩 입력받는다.
data = [int(input()) for _ in range(N)] # 입력받은 data는 list 형태로 저장한다.

pwd = str(sum(data)) # 입력받은 data를 모두 더한 후 string으로 변환하고 pwd 변수에 저장한다.

for i in range(10):
    print(pwd[i], end='') # pwd에 저장된 입력된 모든 데이터의 합을 앞에서 10자리 수를 체크 암호로 출력해준다.