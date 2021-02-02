from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.inbound = 0  # 유입 간선
        self.children = []

    def push(self, v):
        self.children.append(v)
        self.children.sort(reverse=True)


n, m = map(int, input().split())
order, processNext = [], deque()
students = [Node(i) for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    students[a-1].push(b-1)
    students[b-1].inbound += 1

for i in range(len(students)-1, -1, -1):
    if students[i].inbound == 0:
        processNext.append(students[i])

while len(processNext) > 0:
    node = processNext.popleft()
    for c in node.children:
        students[c].inbound -= 1
        if students[c].inbound == 0:
            processNext.append(students[c])
    order.append(node.data+1)

print(" ".join(map(lambda x: str(x), order)))

# Q. 위상정렬 개념을 보고 풀었는데, 문제에서 요구하는 부분에서 제가 놓친게 있을까요...?
