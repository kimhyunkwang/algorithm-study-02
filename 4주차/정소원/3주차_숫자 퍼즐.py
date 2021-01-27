# 진법으로 하는 것 같긴한데...뭔가 수학적인 느낌없이 패턴 구해서 야매로 구현함..경우의 수 더 많아지면 터질듯
K = int(input())

puzzle = ['4', '7']

i = 0
while len(puzzle) < K:
    puzzle.append(puzzle[i]+'4')
    puzzle.append(puzzle[i]+'7')
    i += 1

print(puzzle[K-1])
