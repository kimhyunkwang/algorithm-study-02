# 도도새의 업무일지

# 업무일지 B의 길이 N을 입력받기
N = int(input()) 

# 업무일지 B를 이루는 N개의 정수를 공백을 사용해서 한 번에 입력받고, list로 저장
b = [int(x) for x in input().split()] 

a = [] # 업무일지 A

i = 0

while True:
    # 업무일지 A 리스트에 복구된 값 추가
    # a[i] = (b[i] * (i+1)) - sum(a[:i])
    a.append((b[i] * (i+1)) - sum(a[:i]))
    i += 1
    if i == N: # A의 업무일지 길이가 B의 업무일지 길이와 같으면
        break

for i in range(N):
    # 업무일지 A 리스트 내 원소를 출력 예시에 맞도록 공백을 넣어서 출력
    print(a[i], end = ' ')