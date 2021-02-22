# 0-1 배낭문제
N, K = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(N)]
pack = [[] for i in range(N + 1)]

# 물건의 개수 n
for n in range(N + 1):
    for c in range(K + 1): # 현재 가방 무게 c
        if n == 0 or c == 0:
            pack[n].append(0)
        elif things[n - 1][0] <= c: # 현재 물건 [n-1][0] == 무게값([n-1][1] == 가치)이 배낭의 용량보다 작을 때
            pack[n].append(
                max(
                    things[n - 1][1] + pack[n - 1][c - things[n - 1][0]], pack[n - 1][c]
                ) # max(현재 물건의 가치 + 무게를 가득 채울 수 있는 경우의 가치, 현재 물건을 담지 않았을 때의 최고 가치)
            )
        else:
            pack[n].append(pack[n - 1][c])

print(pack[N][K])
# print(max([max(p) for p in pack]))
