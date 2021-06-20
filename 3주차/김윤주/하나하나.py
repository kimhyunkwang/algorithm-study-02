s = input().upper()   #대문자로 변환

count = dict()   #dict 생성
for word in s:
    count[word] = count.get(word,0)+1   #알파벳 세기

a = sorted(count.items(),key=(lambda item:item[1]), reverse=True)   #많이 쓰인 순서대로 정렬

if len(count) > 1 and a[0][1] == a[1][1]:
    print('?')
else:
    print(a[0][0])