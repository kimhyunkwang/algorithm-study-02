blue = sum(map(int, input().split()))
white = sum(map(int, input().split()))

if blue >= white:
    print(blue)
else:
    print(white)