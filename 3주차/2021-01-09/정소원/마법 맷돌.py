s, t = [input() for i in range(2)]


def solution(s, t):
    if len(s) >= len(t):
        mx, mn = s, t
    else:
        mx, mn = t, s
    j = 0
    for i in range(len(mx)):
        if mx[i] != mn[j]:
            return 0
        j = (j+1)%len(mn)
    return 1

print(solution(s*2, t*2))
# abaabaabaabac
# aba