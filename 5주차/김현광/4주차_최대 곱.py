s, k = map(int, input().split())

q = s // k
r = s % k
ans = (q**(k-r)) * (q+1)**r

print(ans)