# [BFS] 범인 찾기

N, K = map(int, input().split())

# 섹터의 모든 위치를 False로 채운 리스트
visited = [False for i in range(100001)]

def bfs(start, end):
    # 탐색한 위차와 시간을 튜플로 담은 pos_time 리스트 생성
    pos_time = [(start, 0)]
    # 범인을 찾는 가장 이른 시간을 나타내는 변수 min_time
    min_time = 100001
    while len(pos_time) > 0:
        # pos_time 리스트의 0번째 index에 위치한 튜플 (position, time)을 리스트에서 제거 후
        # 그 리스트의 position에 해당하는 cur과 그 위치에 있을 때 시간에 해당하는 time을 지정
        cur, time = pos_time.pop(0)
        
        # 현재 위차가 범인의 위치일 때
        if cur == end:
            # 현재 위치에 도착하기 까지 걸린 시간을 min_time에 입력
            min_time = min(time, min_time)
        
        # 현재 위치 cur에서 다음 위치로 갈 수 있는 경우인 cur*3, cur+1, cur-1를 생각
        nxt_cur = [cur*3, cur+1, cur-1]
        
        for i in nxt_cur:
            # 다음 위치가 주어진 섹터 범위 내에 있고 방문하지 않았다면
            if (i >= 0 and i <= 100000) and not visited[i]:
                # pos_time에 다음 위치와 현재 위치까지 오는데 걸린 시간에 1을 더한 튜플을 추가
                pos_time.append((i, time+1))
                # 아직 방문하지 않았으므로, 해당 위치의 visited 리스트의 인덱스 값을 True로 변경
                visited[i] = True
                
    return min_time

print(bfs(N, K))