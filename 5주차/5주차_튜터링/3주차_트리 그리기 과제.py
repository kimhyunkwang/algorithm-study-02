n, m = map(int, input().split())


class Node:
    def __init__(self, data):
        self.children = []
        self.data = data

    def push_children(self, data):
        self.children.append(data)


tree = [Node(i) for i in range(n)]
if n-m-1 > m:  # 터미널 노드의 수보다 중간에 들어가야할 노드 수가 많을 때
    j = n-m
    for i in range(1, m+1):
        tree[0].push_children(i)
        p, c = i, i+m
        while c < n-m:
            tree[p].push_children(c)
            p, c = c, c+m
        tree[p].push_children(j)
        j += 1
else:  # 터미널 노드 수와 중간 노드 수가 같거나 적을 때
    j = n-m  # n-m 터미널 노드의 시작점
    for i in range(1, n-m):  # 터미널 노드 이전까지 중간 단계에 있는 노드들을 탐색
        tree[0].push_children(i)  # 해당 노드들을 모두 root 노드(0)에 연결
        if j < n:  # 터미널 노드를 모두 연결했다면
            tree[i].push_children(j)
            j += 1
    for k in range(j, n):
        tree[0].push_children(k)


def print_tree(cur):  # pre-order 순회
    for n in tree[cur].children:
        print(cur, n)
        print_tree(n)


print_tree(0)

# 3주차 문제 브루스포스 - 트리 그리기 과제 문제입니다.
# Q. 문제에서 말하는 사전적으로 우선순위에 있는 트리는 무엇인가요?
# Q. 터미널 노드(리프노트)를 n-1 부터 n-m까지의 수로 두고 중간 단계를 차례대로 채워나가는 식으로 구현했는데..80점이 나옵니다..어떤 부분이 틀린것일까요..?
