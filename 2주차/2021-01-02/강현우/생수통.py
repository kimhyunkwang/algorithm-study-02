bottle, cap = [], []
for i in range(3):
    bottle.append(int(input()))
for i in range(2):
    cap.append(int(input()))
print(min(bottle) + min(cap) + 10)