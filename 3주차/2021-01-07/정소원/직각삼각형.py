def pythagoras(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    return False


while True:
    sides = input()
    if sides == '0':
        break
    a, b, c = map(lambda x: int(x), sides.split())
    # 피타고라스 정의
    if pythagoras(a, b, c):
        print("rightangle")
    else:
        print("triangle")
