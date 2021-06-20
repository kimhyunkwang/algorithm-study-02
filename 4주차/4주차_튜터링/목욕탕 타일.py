# 정소원 코드 추가 - 최대 정사각형 크기로 채우는 방법으로 구현했지만, 반례가 존재(60)
N, M = [int(input()) for _ in range(2)]


def getSquareNum(r, c):
    n, m = min(r, c), max(r, c)
    if n == 0:
        return 0
    return m//n + getSquareNum(n, m % n)


print(getSquareNum(N, M))
# Q. DP문제인것 같은데 점화식 규칙을 못 찾겠습니다...!
