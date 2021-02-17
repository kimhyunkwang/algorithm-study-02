import sys

dad, mom, child = sys.stdin.readline().split()
cache = [False] * len(child)  # child의 문자열에 대한 탐색 여부를 저장할 캐시


def ckChildName(cs, ps, p):
    j = 0
    for i in range(len(child)):
        if child[i] == p[j] and not cache[i]:  # 아직 방문하지 않은 문자에 대해 유효한지 판단
            cache[i] = True
            j += 1
        if j >= len(p):
            break
    return True if j == len(p) else False


# child의 모든 문자(vertex)가 부모의 vertex와 일치하는지 확인
if ckChildName(0, 0, dad) and ckChildName(0, 0, mom):
    print("yes")
else:
    print("no")
