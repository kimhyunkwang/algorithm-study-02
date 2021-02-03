# 5주차 알고리즘 

n, m = map(int, input().split())
 
for i in range(n - m): # 루트 노드에 연결
	print(i, i + 1)
for i in range(n - m, n - 1): # 리프노드를 맞추기 위한 연결
	print(0, i + 1)