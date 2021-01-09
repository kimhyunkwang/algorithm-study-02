# 유효한 () bracket 구분하기
bracket = input()

st = []


def ckValidBracket(barcket):

    for c in bracket:
        if c == '(':
            st.append(st)
        else:
            # 짝을 맞출 ( 가 없음
            if len(st) == 0:
                print("NO")
                return
            st.pop()
    if len(st) == 0:
        print("YES")
    else:
        print("NO")


ckValidBracket(bracket)
