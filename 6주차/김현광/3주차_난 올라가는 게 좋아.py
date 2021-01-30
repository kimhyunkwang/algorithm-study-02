n = int(input())
points = []

for i in range(n):
    points.append(tuple(map(int, input().split())))

sorted_points = sorted(points, key=lambda point:(point[1], point[0]))

for point in sorted_points:
    print(point[0], point[1])