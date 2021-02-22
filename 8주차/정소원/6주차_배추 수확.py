N = int(input())
crops = [tuple(map(int, input().split())) for _ in range(N)]
cache = [-1] * (N + 1)

for i in range(N - 1, -1, -1):  # 마지막 날부터 탐색해서 cache에 넣기
    t, p = crops[i]
    cache[i + 1], mx = 0, p
    if i + t > N:  # 수확날짜가 마감일 이후이면, 해당 수확일의 이익은 0이다.
        continue
    for j in range(i + t + 1, N + 1):  # 해당 날짜의 수확이 끝나는 날부터,
        mx = max(p + cache[j], mx)  # 가능한 경우에 대한 최댓값을 구한다.
    cache[i + 1] = mx

print(max(cache))
