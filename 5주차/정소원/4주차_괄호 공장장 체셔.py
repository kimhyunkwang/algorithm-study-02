# 정답코드(튜터님 코드 참고)
N = int(input())
bracket = input()


def ckValidBracket(b):
    stack, mx = [-1], 0
    for i in range(N):
        if b[i] == "(":  # 유효한 ( 괄호열이면
            stack.append(i)  # 해당 인덱스를 스택에 넣습니다.
        else:
            cur = stack.pop()  # ) 괄호의 짝이 맞는 인덱스를 pop합니다.
            if len(stack) == 0:  # 유효하지 않은 괄호열이면
                stack.append(i)
            else:
                # 유효한 괄호열이면,
                # 이전 비유효 괄호열 전까지의 길이를 구해 최댓값에 넣습니다.
                mx = max(mx, i - stack[-1])
    return mx


print(ckValidBracket(bracket))

# 오답노트(틀린이유분석)
# 유효한 괄호가 0일경우와 (()())형태를 걸러주지 못하는 반례가 발생했다.
# 사실상 보기로 주어진 1,2,3 조건을 응용해야되는줄 알고 작성했는데
# 부분문자열을 거르기에도 너무나 부실한 코드였다.
N = int(input())
bracket = input()


def findBracket(b):
    index, idx = [], -1
    while True:
        idx = b.find("()", idx + 1)
        if idx == -1:
            break
        index.append((idx, idx + 1))
    return index


# 특정 문자열 찾기 코드 참고 : https://ponyozzang.tistory.com/447
def getMaxLengthBracket(b):
    mx, index = 0, findBracket(b)
    final = []
    for i, idx in enumerate(index):
        s, e = idx
        # 2번을 만족하는 최대 문자열이 있는지 ck
        while s - 1 >= 0 and e + 1 < len(b):
            if b[s - 1] == "(" and b[e + 1] == ")":
                s, e = s - 1, e + 1
            else:
                break
        if len(final) == 0 or final[-1][1] + 1 < s:
            final.append([s, e])
        else:
            final[-1][1] = e
        # (final)
    arr = sorted([e - s + 1 for s, e in final], reverse=True)
    return arr[0]


print(getMaxLengthBracket(bracket))
