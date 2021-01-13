s = input()
t = input()

def rock(a, b):   #in을 사용하여 서로 해당문자가 있는지 확인
    if a in b:
        return 1
    elif b in a:
        return 1
    else:
        return 0

print(rock(s,t))