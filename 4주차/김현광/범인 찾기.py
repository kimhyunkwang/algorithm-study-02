# test case 2, 4 실패
n, k = map(int, input().split())

if n >= k:
    print(n-k)
else:
    time = 0
    distance = []

    while (True):
        three_times = 3 * n
        minus = n - 1
        plus = n + 1
        
        # 이동했다 가정했을 때 범인과의 거리
        distance = [abs(k - three_times), abs(k - minus), abs(k - plus)]
        
        # 범인과 거리가 가장 가까운 항목의 인덱스
        index = distance.index(min(distance))

        if index == 0:
            n = three_times # 경찰이 three_times 방법을 사용하여 위치 이동
        elif index == 1:
            n = minus # 경찰이 minus 방법 사용하여 위치 이동
        else:
            n = plus # 경찰이 plus 방법 사용하여 위치 이동
            
        # 한 번 이동할 때마다 1초 증가
        time += 1
        
        # 경찰과 범인의 위치가 같아지면 종료
        if n == k:
            break

    print(time)