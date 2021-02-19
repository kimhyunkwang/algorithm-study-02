A, B, C, D = map(int, input().split())
dodo, caterpillar, cheshire = map(int, input().split())

def sensor(n):
    cnt = 0
    if 0 < n % (A + B) <= A:
        cnt += 1
    if 0 < n % (C + D) <= C:
        cnt += 1
    return cnt

print(sensor(dodo))
print(sensor(caterpillar))
print(sensor(cheshire))