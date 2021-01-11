N = int(input())
members = [tuple(input().split()) for _ in range(N)]

res = sorted(members, key=lambda x: (int(x[0]), x[1]))
for m in res:
    print(m[0], m[1])