import datetime
import time

def getDay(a,b,c):
    daylist = ['월', '화', '수', '목', '금', '토', '일']
    return daylist[datetime.date(a,b,c).weekday()]

day = {"월":0, "화":0, "수":0, "목":0, "금":0, "토":0, "일":0}

for i in range(1901,2001):
    for j in range(1,13):
        day[getDay(i,j,1)] += 1

N = int(input())

if N == 0:
    print(day["일"])
elif N == 1:
    print(day["월"])
elif N == 2:
    print(day["화"])
elif N == 3:
    print(day["수"])
elif N == 4:
    print(day["목"])
elif N == 5:
    print(day["금"])
else:
    print(day["토"])