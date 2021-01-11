# Problem Solving

## 개요

- Problem : 피보나치 K번째 수는?
- 문제유형 : 수학
- 난이도 : Level 2
- code : [피보나치 K번째 수는?.py](https://kdt-gitlab.elice.io/yjk5309/algorithm-study-02/-/blob/master/3주차/2021-01-09/정소원/피보나치%20K번째%20수는?.py)

## 풀이방법

- 피보나치 공식인 fibo(n) = f(n-1)+f(n-2)를 기반으로 재귀 형태로 구현하였습니다. 또한, 중복 연산이 계속 적으로 발생하므로 cache에 fibo(n)값을 저장하였습니다.(메모제이션)
- 파이썬은 기본 재귀 제한이 1000(아마도..)이므로 주어진 N만큼의 재귀를 돌기 위해 재귀 제한 횟수를 증가시켰습니다.
- **`Time Complexity`** O(N)
