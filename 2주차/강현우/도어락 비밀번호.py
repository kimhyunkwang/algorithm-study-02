cat, elice = map(int, input().split())
cat, elice  = str(cat), str(elice)
cat_rev, elice_rev = cat[::-1], elice[::-1]
ans = int(cat_rev) + int(elice_rev)
print(ans)