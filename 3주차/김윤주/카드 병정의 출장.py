from itertools import combinations     #combinations 사용

n, m = map(int,input().split())

n_list = list(range(1,n+1))

for i in combinations(n_list, m):
    print(' '.join(map(str, list(i))))


'''
- 반복 가능한 객체(=길이가 n인)에 대해서 중복을 허용하지 않고 m개를 뽑는다.
- 어떤 것을 뽑는지만 중요하게 보기 때문에 뽑은 순서는 고려하지 않는다.
- combinations(반복 가능한 객체, m) 


#출처: https://juhee-maeng.tistory.com/91 [BIU] '''