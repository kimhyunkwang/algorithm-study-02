C, S, E = map(int, input().split())

returned = 0
while returned < E:
    if C//2 <= S:   # 젓가락 set 개수가 숟가락 set 개수보다 적을 때 ➡️ 최대 set값 = 젓가락set 개수
        while C//2 <= S:
            returned += 1
            S -= 1
            if returned == E:
                break
    else:   # 숟가락 set 개수가 젓가락 set 개수보다 적을 때 ➡️ 최대 set값 = 숫가락set 개수
        while C//2 > S:
            returned += 1
            C -= 1
            if returned == E:
                break

if C//2 <= S:
    print(C//2)
else:
    print(S)
