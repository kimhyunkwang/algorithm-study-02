l = []

for i in range(3):                        #3줄이상 넘어가지 않는 조건
    t = list(map(int, input().split()))
    t.sort(reverse=True)                  #제일 큰 수를 앞에 배치
    if 0 in t:                            #0이 있으면 break
        break
    l.append(t)

for i in l:
    if i[0]**2 == i[1]**2+i[2]**2:        #직각삼각형의 조건
        print('rightangle')
    else:
        print('triangle')