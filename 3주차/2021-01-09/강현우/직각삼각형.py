triangle= []
while True:
    end = list(map(int, input().split()))
    if 0 in end:
        break
    triangle.append(end)

for i in triangle:
    j = list(i)
    j.remove(max(i))
    j.remove(min(i))
    if max(i)**2 == min(i)**2 + j[0]**2:
        print("rightangle")
    else:
        print("triangle")