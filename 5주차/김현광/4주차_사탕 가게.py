from math import log2

n = int(input())
candy_list = [n]

while True:
    if n == 1:
        break

    if n % 2 == 0:
        n = n // 2
        candy_list.append(n)
    else:
        n = n * 3 + 1
        candy_list.append(n)

    if (log2(n) - int(log2(n)) == 0):
        break

print(max(candy_list))