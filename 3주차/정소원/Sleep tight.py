import math
x, y, h = map(int, input().split())

print(math.ceil((2*h-y)/(x-y)))