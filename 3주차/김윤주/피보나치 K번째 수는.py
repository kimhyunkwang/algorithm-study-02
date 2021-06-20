k = int(input())

a= [1,1]                           #초기 리스트

for i in range(k):
    if i ==0 or i ==1:             #초기 값은 넘어가도록 설정
        continue
    else:
        a.append(a[i-2]+a[i-1])    #바로 앞 두 항의 합 구현

print(a[k-1])