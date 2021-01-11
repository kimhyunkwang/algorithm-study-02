N, answer = int(input()), input()
#print(N, answer)

def countGrade(s, answer):
    res = 0
    for i in range(len(s)):
        if answer[i] == s[i]:
            res += 1
    return res

blue = '54321'*(N//5) + '54321'[0:N%5]
red = '12345'*(N//5) + '12345'[0:N%5]
yellow = '3'* N

score = [(countGrade(red, answer), 'red'), (countGrade(blue, answer), 'blue'), (countGrade(yellow, answer), 'yellow')]
score = sorted(score, key=lambda x: x[0], reverse=True)
print(score[0][0])
for i in range(3):
    if score[0][0] == score[i][0]:
        print(score[i][1])
