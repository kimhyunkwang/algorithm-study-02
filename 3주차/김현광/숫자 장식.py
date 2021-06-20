n, m = map(int, input().split())

if m == 1:
    for i in range(1, n+1):
        print(i)
elif m == 2:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i, j)
elif m == 3:
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                print(i, j, k)
elif m == 4:
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                for a in range(1, n+1):
                    print(i, j, k, a)
elif m == 5:
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                for a in range(1, n+1):
                    for b in range(1, n+1):
                        print(i, j, k, a, b)
elif m == 6:
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                for a in range(1, n+1):
                    for b in range(1, n+1):
                        for c in range(1, n+1):
                            print(i, j, k, a, b, c)
else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                for a in range(1, n+1):
                    for b in range(1, n+1):
                        for c in range(1, n+1):
                            for d in range(1, n+1):
                                print(i, j, k, a, b, c, d)