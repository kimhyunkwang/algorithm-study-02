# 바쁘다 바빠

# 각 경로에서 걸린 초를 4가지 경우로 입력 받는다.
ab = int(input())
bc = int(input())
cd = int(input())
da = int(input())

total = ab + bc + cd + da 

print(total // 60) # 총 걸린 시간을 60으로 나눈 몫을 반환(분)
print(total % 60) # 총 걸린 시간을 60으로 나눈 나머지를 반환(초)