N, K = map(int, input().split())
soldiers = list(map(int, input().split()))


def getSmallestArr():
    pointer = [i for i in range(N) if soldiers[i] == 1]  # 오름차순으로 정렬된 포인터 list
    if len(pointer) < K:
        return -1
    if len(pointer) == K:
        return max(pointer)-min(pointer)+1
    # 고정된 k 크기의 슬라이딩 윈도
    i, j, res = 0, K-1, N
    while j < len(pointer):
        res = min(pointer[j]-pointer[i]+1, res)
        i = i+1
        j = i+K-1
    return res


if __name__ == "__main__":
    print(getSmallestArr())
