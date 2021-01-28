n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
    result.append(1)

for i in range(n-1):
    for j in range(i+1, n):
        if (m[i][0] > m[j][0]):
            if (m[i][1] > m[j][1]):
                result[j] += 1
            else:
                continue
        elif (m[i][0] < m[j][0]):
            if (m[i][1] < m[j][1]):
                result[i] += 1
            else:
                continue
                
for i in range(len(result)):
    print(result[i], end = ' ')

# 등수를 다 1로 설정해 놓은 다음 
# 리스트의 0~n-1 (앞에서부터 비교) 1~n(비교 대상)을 비교하면서
# 등수가 낮게 나와야 하는 점수에 +1을 해준다