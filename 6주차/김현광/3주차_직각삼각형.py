triangle_list = []

while (True):
    if len(triangle_list) != 0 and triangle_list[-1][0] == 0:
        break
    triangle_list.append(list(map(int, input().split())))

for triangle in triangle_list[:-1]:
    triangle = sorted(triangle)
    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
        print("rightangle")
    else:
        print("triangle")