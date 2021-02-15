import sys

dad, mom, child = sys.stdin.readline().split()
cache = [False] * len(child)


def ckChildName(cs, ps, p):
    j = 0
    for i in range(len(child)):
        if child[i] == p[j] and not cache[i]:
            cache[i] = True
            j += 1
        if j >= len(p):
            break
    return True if j == len(p) else False


if ckChildName(0, 0, dad) and ckChildName(0, 0, mom):
    print("yes")
else:
    print("no")