# 주방장 도도새

N, T = map(int, input().split())

order = [int(x) for x in input().split()]

sum_time = 0

i = 0

while True:
    sum_time += order[i]
    i += 1
    if sum_time > T: 
        print(i-1)
        break
    elif i == N:
        print(i)
        break