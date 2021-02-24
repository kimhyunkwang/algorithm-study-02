N = int(input())

res = N
for i in range(1, N - 2):
    res = max(res, i * (N - i - 1))
print(res)

# Q. 이 문제는 DP로 어떻게 풀어가야하는지 몰라서,
# 그냥 Crtl-A, Ctrl-C, Ctrl-V 3회 누르는 경우에서 가장 큰 값을 구해주는 식으로 구현했는데
# 3개의 2, 3, 5번 case에서 오답이어서, 놓친 경우의 수가 있는 것인지와 DP로 어떻게 접근해야하는지 궁금합니다.
