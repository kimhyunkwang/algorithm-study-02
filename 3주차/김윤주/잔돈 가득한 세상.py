n = int(input())

x = 10000-n

m = [1000,100,10,1]

sum=0
for i in m:
    if i <= x:
        a = x//i
        x -= i*a
        sum += a

print(sum)