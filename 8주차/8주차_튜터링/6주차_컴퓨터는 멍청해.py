# 5번 케이스에서 배열 인덱스 참조 에러 발생
n = int(input())
k = list(map(int, input().split()))
cache = [-1] * n

for i in reversed(range(n)):
    cur, cache[i] = k[i], k[i]
    for j in range(i + 1, n):
        if cache[j] != -1:
            if cur + cache[j] > cache[i]:
                cache[i] = cur + cache[j]
                break
        if cur + k[j] < cache[i]:
            break
        cur += k[j]
        cache[i] = cur

print(max(cache))

# 아래는 모든 케이스 통과
n = int(input())
k = list(map(int, input().split()))
cache = [-1] * (len(k))

for i in reversed(range(len(k))):
    cur, cache[i] = k[i], k[i]
    for j in range(i + 1, len(k)):
        if cache[j] != -1:
            if cur + cache[j] > cache[i]:
                cache[i] = cur + cache[j]
                break
        if cur + k[j] < cache[i]:
            break
        cur += k[j]
        cache[i] = cur

print(max(cache))

# [확인 해봐주셨으면 하는것...!]
# 문제에서 n개의 수열 k(n)이 주어진다고 했으므로 n = len(k)여야 한다고 생각하는데,
# 막상 문제를 풀 때, range(n)을 기준으로 탐색하면 5번 케이스에서 index 참조 에러가 발생합니다.
# len(k)를 기준으로 배열을 탐색하면 정답처리가 되는 것을 보니, n < len(k)인 경우가 주어지는 것이라고 생각해서요
# 코드에 문제가 있는 것이 아니라면 테스트 케이스 확인을 부탁드려도 될까요!?
