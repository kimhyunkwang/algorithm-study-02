# 정소원 풀이 코드 추가
# 접근법이 틀린것 같습니다.(40)
N = int(input())
bracket = input()


# def ckValidBracket(b):
#     stack, res = [], 0
#     for c in b:
#         if c == '(':
#             stack.append(0)
#         else:
#             if len(stack) == 0:
#                 return False
#             stack.pop()
#     if len(stack) != 0:
#         return False
#     return True


def findBracket(b):
    index, idx = [], -1
    while True:
        idx = b.find('()', idx+1)
        if idx == -1:
            break
        index.append((idx, idx+1))
    return index

# 특정 문자열 찾기 코드 참고 : https://ponyozzang.tistory.com/447


def getMaxLengthBracket(b):
    mx, index = 0, findBracket(b)
    final = []
    for i, idx in enumerate(index):
        s, e = idx
        # 2번을 만족하는 최대 문자열이 있는지 ck
        while s-1 >= 0 and e+1 < len(b):
            if b[s-1] == '(' and b[e+1] == ')':
                s, e = s-1, e+1
            else:
                break
        if len(final) == 0 or final[-1][1] + 1 < s:
            final.append([s, e])
        else:
            final[-1][1] = e
        # (final)
    arr = sorted([e-s+1 for s, e in final], reverse=True)
    return arr[0]


print(getMaxLengthBracket(bracket))
# Q. 스택으로 문제 해결하는 방법, 유효한 문자열 단위로 끊어서 분할 재귀로 풀어야 할까요...?
