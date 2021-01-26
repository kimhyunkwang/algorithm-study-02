n, k = map(int, input().split())
soldiers = list(map(int, input().split()))

def indexing(ls, element):
    index_list = []
    for i in range(len(ls)):
        if ls[i] == element:
            index_list.append(i)
    return index_list

if soldiers.count(1) < k:
    print(-1)
else:
    index_list = indexing(soldiers, 1)
    cases = len(index_list) - k + 1
    sizes = []
    for i in range(cases):
        size = index_list[i+k-1] - index_list[i] + 1
        sizes.append(size)
    print(min(sizes))