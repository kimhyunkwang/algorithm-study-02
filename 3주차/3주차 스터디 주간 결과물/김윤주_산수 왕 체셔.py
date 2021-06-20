a, b, c = map(int, input().split())

answer = a**b%c

print(answer)

#2개의 test case에서 시간초과
#분할정복 문제인데 어떤식으로 분할해야되는지 궁금합니다