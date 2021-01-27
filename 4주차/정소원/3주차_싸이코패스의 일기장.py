# 정수론이란 뭔상관..정수론으로 어케품...? 예시 잘못나옴(A->E, B->F)
S = input()

alpha = [chr(ord('A')+i) for i in range(26)]
alpha = alpha[-4:] + alpha[0:-4]

res = ''
for ch in S:
    res += alpha[ord(ch)-ord('A')]
print(res)
