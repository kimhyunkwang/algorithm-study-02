# 생수통

# 각 물통과 뚜껑의 가격을 입력받는다.
bottle_1 = int(input())
bottle_2 = int(input())
bottle_3 = int(input())
lid_1 = int(input())
lid_2 = int(input())

# 물통과 뚜껑 각각의 최솟값이 가격을 bottle와 lid 변수에 저장
bottle = min(bottle_1, bottle_2, bottle_3)
lid = min(lid_1, lid_2)

# 샘물의 가격
sammul = bottle + lid + 10

print(sammul)