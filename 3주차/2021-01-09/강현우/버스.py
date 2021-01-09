from math import gcd 

def lcm(A, B): 
    return A * B // gcd(A,B) 
    
A, B = map(int,input().split())

print(lcm(A,B))
