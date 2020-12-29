# :pencil: Week2 코드 리뷰

### :round_pushpin: 알람 시계 - 2884

### :round_pushpin: 평균 - 1546

- map(함수, 리스트)

  `map(lambda x : x표현식, 리스트)` : map function 사용시에는 lambda 사용할 것

### :round_pushpin: 열개 출력 - 11721

- 소수점 함수

  - ceil() : 소수점을 무조건 올림(실수를 정수로 만듬)
  - floor() : 소수점 아래로 무조건 무시
  - round() : 반올림 함수

  ```python
  ceil(99.2)=100
  floor(3.6)=3
  round(3.4)=3
  round(5.6)=6
  ```

- 연산

  - / : 나눗셈(실수 반환)
  - // : 몫
  - % : 나머지

- 출력
  - end="" : 뒤에 출력값에 이어서 출력(줄바꿈x)
  - sep="@" : 영단어를 분리하여 출력(사이에 @가 들어감)

### :round_pushpin: 일곱 난쟁이 - 2309

- 변수
  `global sevenP`
  
  while문 밖에서도 리스트를 사용하기 위해 global 붙이기(전역변수 값 변경가능)

- 리스트에서 랜덤 추출 `import random`

  - random.choice(리스트) : 리스트 내 1개만 랜덤으로 추출
  - random.sample(리스트, 갯수) : 리스트 내 여러가지 랜덤으로 추출(중복 허용x)

  ```python
  li=[1,2,3]
  choiceList = random.choice(li)
  choiceList2 = random.sample(li, 2) # 2개 랜덤 추출
  choiceList2 = random.sample(li, 4) # 컴파일 에러
  choiceList3 = [random.choice(li) for i in range(2)] # 리스트에서 2개 랜덤 추출(중복 허용)
  ```

- 입력 `import sys`

  input() 대신 **sys.stdin.readlin()** -> 시간적 효율성 높아짐(빠르게 입력받고 싶을 때)

- 자료형
  - set 집합: 중복 방지

### :round_pushpin: 달팽이 - 2869

ceil() : 소수점을 무조건 올림(실수를 정수로 만듬)

### :round_pushpin: 1,2,3 더하기 - 9095

`dp` 관련 유형

- 부분 문제가 겹침 (예. 피보나치)
- 최적 부분 구조
- 작은 문제로 큰 문제의 정답을 구할 수 있다 🌈

- 풀이 방법
  - top-down (재귀호출)
  - bottom-up
