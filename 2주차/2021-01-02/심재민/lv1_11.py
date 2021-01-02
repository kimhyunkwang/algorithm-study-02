# 도어락 비밀번호

N1, N2 = map(int, input().split())

reverse_N1 = int(str(N1)[::-1])

reverse_N2 = int(str(N2)[::-1])

ans = reverse_N1 + reverse_N2

print(ans)