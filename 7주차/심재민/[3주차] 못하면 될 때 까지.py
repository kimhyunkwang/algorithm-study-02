# [수학] 못하면 될 때 까지

s = int(input())

for  i in range(1, 2000000000):
    if (i*(i+1))/2 > s:
        print(i-1)
        break
