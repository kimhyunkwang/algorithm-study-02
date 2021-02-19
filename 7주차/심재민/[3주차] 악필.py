# [수학] 악필

a, b = input().split()

mina = a.replace('7', '9')
minb = b.replace('7', '9')

maxa = a.replace('9', '7')
maxb = b.replace('9', '7')

print(int(mina)+int(minb), int(maxa)+int(maxb))