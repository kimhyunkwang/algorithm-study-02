# Problem Solving

## 개요

- Problem : K번 곱하기
- 문제유형 : 구현(Implement), 수학
- 난이도 : Level 1
- code : [K번 곱하기.py](https://kdt-gitlab.elice.io/yjk5309/algorithm-study-02/-/blob/master/2주차/2021-01-03/정소원/K번%20곱하기.py)

## 풀이방법

- 1번방법: 1~N까지 해당 숫자를 K제곱하여 더해주었습니다.
- 2번방법: (홀수 거듭제곱합) + 2^K(짝수 거듭제곱합)을 통한 재귀로 구현하였습니다.
- 1번 방법에서 반복문 수행횟수를 줄여보려고 하였지만 똑같은 O(NlogN)으로 구성되었고, 2가지 문항은 시간초과를 받았습니다. 정답과 관계없이 O(N)번으로 반복문을 돌려도 시간초과가 뜨는 것을 보니 O(N)이하의 구현방법을 찾아봐야할 것 같습니다.
- **`Time Complexity`** O(NlogN)
