n = int(input())

week = [0 for i in range(7)]

for year in range(1901, 2001):
    for month in range(1, 13):
        if month == 1:
            if year == 1901:
                start_day = 2
            else:
                start_day += 3
        elif month == 3:
            if year % 4 == 0:
                start_day += 1
            else:
                start_day += 0
        elif month in (2, 4, 6, 8, 9, 11):
            start_day += 3
        elif month in (5, 7, 10, 12):
            start_day += 2

        start_day = start_day % 7
        week[start_day] += 1

print(week[n])