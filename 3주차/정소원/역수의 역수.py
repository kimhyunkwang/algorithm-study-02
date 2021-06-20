n1, n2 = map(int, input().split())

def getInverse(n):
    return int(str(n)[::-1])

print(getInverse(getInverse(n1)+getInverse(n2)))