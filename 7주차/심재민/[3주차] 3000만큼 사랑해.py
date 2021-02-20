# [수학] 3000만큼 사랑해

n = input()

count = {}

for i in n:
    try:
        count[i] += 1
    except:
        count[i] = 1
        
if (max(count, key=count.get) == '6') or (max(count, key=count.get) == '9'):
    print(int(count['6']/2))
else:
    print(count[max(count, key=count.get)])