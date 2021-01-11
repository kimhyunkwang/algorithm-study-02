# kmp
N = input()

def getfailure(p):
    arr = [0 for i in range(len(p))]
    j = 0
    for i in range(1,len(p)):
        while j > 0 and p[i] != p[j]:
            j = arr[j-1]
        if p[i] == p[j]:
            j += 1
            arr[i] = j
    return arr

def kmp(s, p):
    failure = getfailure(p)
    res, j = -1, 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = failure[j-1]
        if s[i] == p[j]:
            if j == len(p)-1:
                res = i-len(p)+2
                return res
            else:
                j += 1
    return res
            
s = "".join([str(i) for i in range(1,int(N)+1)])
print(kmp(s, N))