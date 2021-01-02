# 청팀 백팀

# 청팀의 체육대회 종목별 점수를 공백을 사용해 한 번에 입력받기
# b1 = 축구, b2 = 줄다리기, b3 = 단체줄넘기, b4 = 이어달리기
b1, b2, b3, b4 = map(int, input().split())

# 백팀의 체육대회 종목별 점수 입력받기
# w1 = 축구, w2 = 줄다리기, w3 = 단체줄넘기, w4 = 이어달리기
w1, w2, w3, w4 = map(int, input().split())

b_sum = b1 + b2 + b3 + b4 # 청팀의 체육대회 총 점수
w_sum = w1 + w2 + w3 + w4 # 백팀의 체육대회 총 점수

if b_sum > w_sum: 
    print(b_sum)
elif b_sum < w_sum:
    print(w_sum)
else:               # b_sum == w_sum
    print(b_sum)