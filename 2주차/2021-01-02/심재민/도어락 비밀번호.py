# 도어락 비밀번호
# 체셔 고양이와 엘리스가 태어난 연도를 입력한다.
N1, N2 = map(int, input().split())

# 입력받은 N1, N2를 string으로 변환 후 자릿 수를 역순으로 치환한 뒤 다시 integer로 변환해준다.
reverse_N1 = int(str(N1)[::-1])

reverse_N2 = int(str(N2)[::-1])

ans = reverse_N1 + reverse_N2

print(ans)