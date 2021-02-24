N = int(input())

def get_prime(x):
    # 0부터 x까지 초기화 (인덱스를 편하게 사용하기 위해)
    is_prime = [False, False] + [True for i in range(x -1)]
    primes = []
    
    # 2부터 x까지 하나씩 검사
    for i in range(2, x + 1):
        # 소수면 리스트에 추가하고 그 수의 배수는 모두 False로 변경
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, x + 1, i):
                is_prime[j] = False
    return primes

# 2N까지의 소수 구하기
primes = get_prime(N * 2)
count = 0
# 소수 리스트에는 어차피 2N 이하의 수만 있기 때문에 N 초과인 수만 뽑아내는 조건을 걸어주면 된다. 
for i in range(len(primes)):
    if primes[i] > N:
        count += 1

print(count)