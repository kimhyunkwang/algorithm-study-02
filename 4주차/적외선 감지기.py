A, B, C, D = map(int, input().split())
dodo, cater, ches = map(int, input().split())

dodo_data, cater_data, ches_data = 0,0,0

if (dodo % (A+B))-1 < A:
    dodo_data += 1
if (dodo % (C+D))-1 < C:
    dodo_data += 1
if (cater % (A+B))-1 < A:
    cater_data += 1
if (cater % (C+D))-1 < C:
    cater_data += 1
if (ches % (A+B))-1 < A:
    ches_data += 1
if (ches % (C+D))-1 < C:
    ches_data += 1
    
print(dodo_data)
print(cater_data)
print(ches_data)

# 60점이 나오는데 풀이방법이 어디가 틀렸는지 잘 모르겠습니다..