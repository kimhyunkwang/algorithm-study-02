N = int(input())
cache = [-1] * (N + 1)
cache[1], cache[2] = 1, 2

for i in range(3, N + 1):
    cache[i] = cache[i - 1] + cache[i - 2]
print(cache[N])

# Q. 단순하게 최대 길이가 N일때, 끝에 오는 문자가 1일때(cache[i-1])와 00(cache[i-2])일때라고 생각하고 풀이했는데,
# 메모리 초과가 발생하고 오답이 case도 나와서, 어떤 방식으로 풀이해야 하는지 궁금합니다..!
