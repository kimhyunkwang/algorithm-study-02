# [수학] 이번 달 종로는 우리 구역이라고

# 20세기: 1901년 1월 1일부터 2000년 12월 31일
# 1901년 1월 1일 화요일
# 0 : 일 1 : 월 2 : 화 3: 수 4 : 목 5 : 금 6 : 토

weekday = int(input())

days = [0, 1, 2, 3, 4, 5, 6]

isleaf = lambda x: x % 400 == 0 or x % 100 != 0 and x % 4 == 0

day, cnt = 2, 0
for year in range(1901, 2001):
    dom = [0, 31, 28+isleaf(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for month in range(1, 13):
        cnt += (days[day] == weekday)
        day = (day + dom[month]) % 7

print(cnt)