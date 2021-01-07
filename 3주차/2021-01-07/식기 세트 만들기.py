# [그리디] 식기 세트 만들기

C,S,E = map(int, input().split())

if C//2 >= S:
    max_num = S
elif C//2 < S:
    max_num = C//2
    
print(max_num)