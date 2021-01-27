n = int(input())
words = [input() for _ in range(n)]


def encryption(s):
    alpha = [chr(ord('A')+i) for i in range(26)]
    res = ''
    for c in s:
        idx = (ord(c)-ord('A')+1) % 26
        res += alpha[idx]
    return res


for word in words:
    print(encryption(word))
