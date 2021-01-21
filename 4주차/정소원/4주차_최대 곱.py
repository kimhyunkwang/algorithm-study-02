S, K = map(int, input().split())

m, r = S//K, S % K
print(m**(K-r) * (m+1)**r)
