order, working_time = map(int, input().split())
cooking_time = list(map(int, input().split()))
total_cooking_time = 0
count = 0

for i in range(order):
    total_cooking_time += cooking_time[i]
    if total_cooking_time > working_time:
        break

    count += 1

print(count)