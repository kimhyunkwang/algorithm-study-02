# D(n) = (n-1)*(D(n-1)+D(n-2))
N = int(input())
cache = [-1] * 21
cache[1], cache[2] = 0, 1


def solution(n):
    if cache[n] != -1:
        return cache[n]
    cache[n] = (n - 1) * (solution(n - 1) + solution(n - 2))
    return cache[n]


print(solution(N))


# 오답노트(틀린이유분석)
# dfs를 통한 경우의 수 탐색(60) => 시간초과(모든 그래프를 탐색하는 과정에서 시간초과가 발생)
# 그래프에서 규칙적인 값이 생기므로, 해당 영역을 잘 캐치해서 수식으로 정리해보는 연습을 해야 할 듯
# def countWeaponCom(n, cur, res):
#     if len(cur) == n-1:
#         return res+1
#     v = len(cur)
#     for i in range(n):
#         if v == 0 and i > 1:
#             break
#         if v != i and i not in cur:
#             cur.append(i)
#             res = countWeaponCom(n, cur, res)
#             cur.pop()
#     return res

# def countBranch(n):
#     if cache[n] != -1:
#         return cache[n]
#     cache[n] = countWeaponCom(n, [], 0) - countBranch(n-1)
#     return cache[n]
