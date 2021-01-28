N, S = int(input()), input()


def calculate(l, r, op):
    l, r = int(l), int(r)
    if op == '+':
        return str(l+r)
    elif op == '-':
        return str(l-r)
    return str(l*r)


def solution(s, mx):
    if len(s) == 1:
        # print(int(s[0]))
        return max(mx, int(s[0]))
    for i in range(1, len(s), 2):
        if i+1 < len(s)-1:
            nx = s[:i-1]+[calculate(s[i-1], s[i+1], s[i])]+s[i+2:]
        else:
            nx = s[:i-1]+[calculate(s[i-1], s[i+1], s[i])]
        mx = solution(nx, mx)
    return mx


print(solution(list(S), 0))

# 3주차 문제 브루스포스 - 조교님, 점수 올려주세요 문제입니다.
# Q. 해결방법은 무엇이고 코드가 틀린 이유는 왜일까요..? 반례가 생각나지 않습니다..ㅠ..
