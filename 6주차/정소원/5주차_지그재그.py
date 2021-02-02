n, r, c = map(int, input().split())


def zigzag(n, cr, cc, res):
    mv = [(0, 0), (0, 1), (1, 0), (1, 1)]
    if n == 2:
        for i in range(4):
            cx, cy = cr+mv[i][0], cc+mv[i][1]
            if cx == r and cy == c:
                print(res)
                return True
            res += 1
    else:
        for i in range(4):
            cx, cy = cr+mv[i][0]*(n//2), cc+mv[i][1]*(n//2)
            if r >= cx and r < cx+(n//2) and c >= cy and c < cy+(n//2):
                if zigzag(n//2, cx, cy, res):
                    break
            else:
                res += (n//2)**2


zigzag(2**n, 0, 0, 0)
