N = int(input())
answer = input()

p = {'red': '12345', 'blue': '54321', 'yellow': '33333'}

max_score = 0

result = {'red': 0, 'blue': 0,'yellow': 0}

for name, pattern in p.items():
    
    score = 0
    
    for i in range(N):
        if answer[i] == pattern[i % len(pattern)]:
            score += 1
            
    if name == 'blue':
        result['blue'] += score
    elif name == 'red':
        result['red'] += score
    else:
        result['yellow'] += score
    
for name, score in result.items():
    
    if score > max_score:
        max_score = score

print(max_score)

first_prize = [name for name, score in result.items() if max(result.values()) == score]

if len(first_prize) > 1:
    for i in first_prize:
        print(i)
else:
    print(first_prize[0])
