# 생수통

bottle_1 = int(input())
bottle_2 = int(input())
bottle_3 = int(input())
lid_1 = int(input())
lid_2 = int(input())

bottle = min(bottle_1, bottle_2, bottle_3)
lid = min(lid_1, lid_2)

sammul = bottle + lid + 10

print(sammul)