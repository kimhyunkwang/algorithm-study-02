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

# input 중에 n개와 다르게 주어지는 경우가 있는듯...?(5번 case)