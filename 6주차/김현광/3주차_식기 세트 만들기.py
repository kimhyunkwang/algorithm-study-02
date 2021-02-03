# c : 젓가락, s : 숟가락, e : 반납할 식기, r : 세트 만들고 남은 나머지
c, s, e = map(int, input().split())

c_pair = c//2

if c_pair < s:
    set = c_pair
    if c % 2 == 0:
        r = s - c_pair
    else:
        r = s - c_pair + 1
else:
    set = s
    r = c - 2*s

while (True):
    if r >= e:
        print(set)
        break
    else:
        set -= 1
        r += 3