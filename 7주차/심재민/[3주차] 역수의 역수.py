# [수학] 역수의 역수

a, b = input().split()

a = a[::-1]
b = b[::-1]

s = int(a) + int(b)

result = str(s)[::-1]

print(int(result))