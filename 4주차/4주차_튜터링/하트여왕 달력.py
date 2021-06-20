from math import gcd 

def lcm(x, y): 
    return x * y // gcd(x,y)

F, W, E = map(int, input().split())

if F==1 and W==1 and E==1:
    print(1)
else:
    print(lcm(lcm(F,E),W))

# 60점이 나오는데 풀이방법이 어디가 틀렸는지 잘 모르겠습니다..