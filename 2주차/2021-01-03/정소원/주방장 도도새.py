N, T = list(map(int, input().split()))
orders = list(map(int, input().split()))
#print(N, T, orders)

total, res = 0, 0

while res < int(N):
    if total+orders[res] < int(T):
        total += orders[res]
        res += 1
    else:
        break

print(res)
