# [구현] 암호 만들기

n = int(input())
words = [input() for _ in range(n)]

def password(word):
    
    result = []
    
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for c in range(len(word)):
    
        if word[c] == 'Z':
            
            result.append('A')
    
        for i in range(len(l)-1):
        
            if word[c] == l[i]:
                
                result.append(l[i+1])
        
    return result

for i in words:
    print(''.join(password(i)))