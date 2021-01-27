# 강현우님 풀이
S = int(input())

ans = 0
# 서로 다른 N개의 합이 최대가 되려면 작은 수부터 더해야 함
for i in range(S+1):
    ans += i
    if ans > S:  # 만약 중간 합이 S보다 커지면 해당 차이만큼의 숫자를 빼줌(N개 개수는 변화-1)
        print(i-1)
        break
    elif ans == S:  # 중간 합이 S와 같으면 해당 N값 출력
        print(i)
        break
