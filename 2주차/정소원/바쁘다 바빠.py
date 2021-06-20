times = 0
for _ in range(4):
    times += int(input())

x, y = times//60, times % 60
print(x, y, sep='\n')
