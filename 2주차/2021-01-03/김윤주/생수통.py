a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())

bottle = min(a, b, c)
lid = min(x, y)

answer = bottle + lid + 10

print(answer)