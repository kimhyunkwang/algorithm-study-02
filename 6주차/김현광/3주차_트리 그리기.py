n, m = map(int,input().split())

# 루트 노드부터 깊게 연결 > 리프노트 1개
for i in range(n-m):
    print(i, i+1)
# 나머지 m - 1개의 리프노드를 만들기 위해 루트 노트에 하나씩 연결
for i in range(n-m, n-1):
    print(0, i+1)