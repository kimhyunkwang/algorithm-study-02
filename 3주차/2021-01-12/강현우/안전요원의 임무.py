from operator import itemgetter

N = int(input())
customer = []

for i in range(N):
    customer.append(list(input().split()))

for i in range(N):
    customer[i][0] = int(customer[i][0])

customer = sorted(customer, key=itemgetter(0,1))

for i in range(N):
    for j in range(2):
        print(customer[i][j], end=" ")
    print()