c, s, e = map(int,input().split())

for i in range(51):
    c = c - 2
    s = s - 1
    if c < 0 or s < 0:               #둘 중 하나가 0보다 작아지면 안되므로 break
        print(i)
        break