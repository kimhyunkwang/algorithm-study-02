S = int(input())

ans = 0
for i in range(S+1):
    if ans > S:
        print(i-2)
        break
    elif ans == S:
        print(i-1)
        break
    ans += i


#  체점 해본결과 한케이스에서 실패가 떴는데 왜 떴는지 잘 모르겠습니다 ㅠㅜ