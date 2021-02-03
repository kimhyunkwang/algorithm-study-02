n = int(input())
ans = input()

q = len(ans) // 5
r= len(ans) % 5

red_ans = "12345" * q + "12345"[:r]
blue_ans = "54321" * q + "54321"[:r]
yellow_ans = "3" * n

def get_score(color_ans):
    score = 0
    for i in range(n):
        if ans[i] == color_ans[i]:
            score += 1
    return score

scores = [get_score(red_ans), get_score(blue_ans), get_score(yellow_ans)]

max_score = max(scores)
print(max_score)

if max_score == scores[0]:
    print("red")
if max_score == scores[1]:
    print("blue")
if max_score == scores[2]:
    print("yellow")