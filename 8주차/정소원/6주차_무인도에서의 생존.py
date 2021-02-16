# 0-1 배낭문제
N, K = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(N)]
pack = [[] for i in range(N + 1)]

for n in range(N + 1):
    for c in range(K + 1):
        if n == 0 or c == 0:
            pack[n].append(0)
        elif things[n - 1][0] <= c:
            pack[n].append(
                max(
                    things[n - 1][1] + pack[n - 1][c - things[n - 1][0]], pack[n - 1][c]
                )
            )
        else:
            pack[n].append(pack[n - 1][c])

print(pack[N][K])
# print(max([max(p) for p in pack]))
