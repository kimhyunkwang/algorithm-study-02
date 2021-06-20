battle = input()

def fight(battle):
    attack, defense = battle.count("("), battle.count(")")

    if attack == defense:
        if battle[-1] == "(":
            return "NO"
        else:
            return "YES"
    else:
        return("NO")
        
print(fight(battle))