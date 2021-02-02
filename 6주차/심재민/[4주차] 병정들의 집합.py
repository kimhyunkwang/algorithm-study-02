# [투 포인터] 병정들의 집합

N, K = map(int, input().split())

soldier_info = list(map(int, input().split()))

def min_size_soldier(lst, value):
    
    index_list = []
    
    sizes = []
    
    for i in range(len(lst)):
        if lst[i] == value:
            index_list.append(i)
    
    if len(index_list) < K:
        return -1
    else:
        cases = len(index_list) - K + 1
        
        for j in range(cases):
            size = index_list[j+K-1] - index_list[j] + 1
            sizes.append(size)
        return min(sizes)

print(min_size_soldier(soldier_info, 1))