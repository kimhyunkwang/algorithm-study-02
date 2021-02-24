from math import floor, sqrt
a, b = map(int, input().split())

def get_prime(n):
    is_prime = [False, False] + [True for i in range(n-1)]
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return primes

def get_prime_fam(primes):
    fam = []
    for num in primes:
        i = 2
        while(True):
            x = num**i
            if b < x:
                break
            if a <= x:
                fam.append(x)
            i += 1
    return fam

N = floor(sqrt(b))
prime_list = get_prime(N)
prime_fam = get_prime_fam(prime_list)
print(len(prime_fam))