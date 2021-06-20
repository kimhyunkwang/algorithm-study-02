fight = input()
villain = fight.count("(")
hero = fight.count(")")

if fight[0] == ")":
    print("NO")
elif villain > hero or villain < hero:
    print("NO")
else:
    print("YES")