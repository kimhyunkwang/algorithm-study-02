bottle_price = []
lid_price = []

for i in range(3):
    bottle_price.append(int(input()))

for i in range(2):
    lid_price.append(int(input()))

answer = min(bottle_price) + min(lid_price) + 10
print(answer)