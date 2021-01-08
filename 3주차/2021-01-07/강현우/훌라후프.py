from math import gcd

num = input()
hool = list(map(int,input().split()))

first_hool = hool[0]

for i in range(1,len(hool)):
    common = gcd(first_hool, hool[i])
    print(f"{first_hool//common}/{hool[i]//common}")