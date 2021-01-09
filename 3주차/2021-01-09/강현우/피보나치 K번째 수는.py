# 방법1
# 3가지 건에 있어서 시간초과
def fib1(num):
    if num <= 1:
        return num
    else:
        return fib1(num-1) + fib1(num-2) 

# 방법2
# 마찬가지로 3가지 건에 있어서 시간초과
fib2 = lambda n: 1 if n<=2 else fib2(n-1) + fib2(n-2)

# 방법3
# maximum recursion error가 났다
# 구글링 했는데 sys로 건드리면 된다하여 그렇게 하였다.
import sys
sys.setrecursionlimit(10**7)

fib3 = lambda n, a=0, b=1 : a if n<=0 else fib3(n-1,b, a+b)

K = int(input())
print(fib3(K))