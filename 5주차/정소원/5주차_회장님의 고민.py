import sys
n = int(input())
budgets = list(map(int, input().split()))
m = int(input())


def get_total(lim):
    total = 0
    for mon in budgets:
        if mon <= lim:
            total += mon
        else:
            total += lim
    return total


def getMaxLimit(s, e):
    mx = 0
    while s <= e:
        lim = (s+e)//2
        total = get_total(lim)
        if total > m:
            e = lim-1
        else:
            mx = max(mx, lim)
            s = lim+1
    return mx


mx, mn = max(budgets), min(m//n, min(budgets))
if sum(budgets) == m:
    print(mx)
else:
    print(getMaxLimit(mn, mx))
