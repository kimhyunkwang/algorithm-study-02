s, t = [input() for i in range(2)]


def solution(s, t):
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            return 0
    return 1


print(solution(s, t))
