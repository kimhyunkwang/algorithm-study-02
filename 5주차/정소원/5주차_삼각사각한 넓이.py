# D(n) = D(n-1) + (D(n-1)-D(n-2))*2
n = int(input())


def _3G4G(n):
    S = [-1]*51
    S[1], S[2] = 1, 2.5
    for i in range(3, n+1):
        S[i] = S[i-1] + (S[i-1]-S[i-2])*2
    return S[n]


print(_3G4G(n))
