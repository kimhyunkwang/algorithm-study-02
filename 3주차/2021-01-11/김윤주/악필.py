a, b = map(str,input().split())     #string으로 받기

max_a = int(a.replace('7','9'))     #replace 사용
max_b = int(b.replace('7','9'))
max = max_a + max_b

min_a = int(a.replace('9','7'))
min_b = int(b.replace('9','7'))
min = min_a + min_b

print(max, min)