n, k = [int(input()) for _ in range(2)]
prime = [True]*(n+1)
prime[0], prime[1] = False, False

for p in range(2, len(prime)):
    if not prime[p]:
        continue
    for i in range(p+p, n+1, p):
        prime[i] = False

primes = [p for p in range(k+1, n+1) if prime[p]]

count = 1  # 1은 무조건 Cut Number
for num in range(2, n+1):
    if prime[num] and k < num:
        continue
    if prime[num] and k >= num:
        count += 1
        continue
    cut = True
    for p in primes:
        if num % p == 0:
            cut = False
            break
    count += (cut)

print(count)

# Q. 시간초과를 피하는 방법은 무엇일까요....!
