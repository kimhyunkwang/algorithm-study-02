# [수학] 훌라후프

N = int(input())
r = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
for i in range(1, N):
    m = gcd(r[0], r[i])
    print("%d/%d" % (r[0]//m, r[i]//m))