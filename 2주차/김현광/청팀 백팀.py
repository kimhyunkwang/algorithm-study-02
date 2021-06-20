blue_scores = list(map(int, input().split()))
white_scores = list(map(int, input().split()))

blue_total = sum(blue_scores)
white_total = sum(white_scores)

if blue_total >= white_total:
    print(blue_total)
else:
    print(white_total)