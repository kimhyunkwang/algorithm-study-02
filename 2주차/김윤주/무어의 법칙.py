n = int(input())

x = str(2**n)
a = []

for i in x:
    a.append(int(i))

print(sum(a))