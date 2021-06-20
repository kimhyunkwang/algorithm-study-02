# 정소원 풀이 코드 추가
# 방법 1: dfs를 통한 경우의 수 탐색(60)
N = int(input())


def countWeaponCom(n, cur, res):
    if len(cur) == n:
        return res + 1
    v = len(cur)
    for i in range(n):
        if v == 0 and i > 1:
            break
        if v != i and i not in cur:
            cur.append(i)
            res = countWeaponCom(n, cur, res)
            cur.pop()
    return res


print(countWeaponCom(N, [], 0) * (N - 1))
# Q. DP 규칙을 못찾겠습니다. 시간복잡도 줄이는 풀이법이 궁금합니다
