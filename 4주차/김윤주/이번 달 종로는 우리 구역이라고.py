import calendar

s = int(input())

if s == 0:
    s = 6
else:
    s -= 1

a = 0

for y in range(1901, 2001):
    for m in range(1,13):
        if calendar.monthrange(y,m)[0] == s:
            a+=1

print(a)

#calendar.monthrange(year, month)은 해당 월의 1일이 무슨 요일(월요일이 0)인지와 해당 월이 며칠까지 있는지를 리턴해줌