# 참고 : https://namu.wiki/w/%ED%8C%8C%EC%9A%B8%ED%95%98%EB%B2%84%EC%9D%98%20%EA%B3%B5%EC%8B%9D
import math
PRIME = 1000000009

def combination(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
    
def mod_power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a % PRIME
    x = mod_power(a, b//2)
    if b % 2 == 1:
        return a*((x*x) % PRIME) % PRIME
    return (x*x) % PRIME
    
def main():
    inp = list(map(int, input().split()))
    N = inp[0]
    K = inp[1]
    k_sums = [0] * (K+1)
    k_sums[0] = N
    for k in range(1, K+1):
        k_sums[k] = mod_power(N+1, k+1) - 1
        #print(k_sums[k])
        for p in range(0, k):
            k_sums[k] -= combination(k+1, p) * k_sums[p] % PRIME
        k_sums[k] *= mod_power(k+1, PRIME-2)
        k_sums[k] %= PRIME
    print(int(k_sums[K]) % PRIME)
if __name__ == "__main__":
    main()