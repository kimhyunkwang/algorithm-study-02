n, k = map(int, input().split())
soldiers = list(map(int, input().split()))

# 병정 리스트에서 다이아몬드 병정(1)이 위치한 모든 인덱스를 구하는 함수
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
    # print(index_list)
    # [0, 4, 6, 9]
    
    cases = len(index_list) - k + 1

    sizes = []
    for i in range(cases):
        size = index_list[i+k-1] - index_list[i] + 1
        sizes.append(size)

    print(min(sizes))

# 다이아몬드의 위치(인덱스)를 찾아주는 함수를 만든 뒤
# 포함되어야 하는 병정의 수에 맞는 제일 짧은 길이의 리스트를 구한다