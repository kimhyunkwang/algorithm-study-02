def isLeapYear(y):
    if y % 4 != 0:
        return False
    elif y % 400 == 0:  # y%4 == 0 and y%400 == 0
        return True
    elif y % 100 == 0:  # y%4 == 0 and y%400 != 0 and y%100 == 0
        return False
    else:  # y%4 == 0 and y%400 != 0 and y%100 != 0
        return True


def countDate(y, m):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        if isLeapYear(y):
            return 29
        else:
            return 28


def countManageDays(d):  # d: 탐색하고자 하는 요일
    res, day = 0, 2  # day: 1901년 1월 1일은 화요일이기 때문에 초기 요알값 2
    for y in range(1901, 2001):  # 1901-2000
        prev = res
        for m in range(1, 13):  # 1-12
            if d == day:
                res += 1
            nxt = countDate(y, m) % 7  # 다음달 1일 요일까지 더해야할 날의 수
            day = (day+nxt) % 7
    return res


def main():
    day = int(input())
    print(countManageDays(day))


if __name__ == "__main__":
    main()
