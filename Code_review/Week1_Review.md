# :pencil: Week1 코드 리뷰

### 별찍기 - 2438
- range(a,b): a에서 b전까지
- 주석 달기 습관!

### N 찍기 - 2438

### 세 수 - 2741
- split(): 공백문자를 기준으로 문자나눔
- map(): int형으로 받기 위해 쓰임
- list(): list 형태로 입력

  **List 함수**
  - sort(): list 오름차순
  - reverse() or sort(reverse=True): list 내림차순

  **내장 함수**
  - sorted() & reversed(): 원본을 변경하지 않는 오름차순, 내림차순

### A+B=3 - 2438


### 숫자의 합 - 2438
1. 
```python
for i in range(0, leng):  # leng대신 (1, leng+1)쓰면 런타임에러남!
    ans += int(nums[i])
```
=> 리스트의 첫번째 인덱스 값은 0부터!!!

- 변수 쓰기 전에 위에서 무조건 변수 선언!!


### 모의고사 - 2438

- **list()** : 배열을 인덱스로 접근해야 함. 
- **enumerate()** : 지연 제너레이터(lazy generator)로 이터레이터 감싸서 이터레이터에서 루프 인덱스와 다음 값을 한 쌍으로 가져와 넘김. 
- for i, val in enumerate(list)
    => i : index, val : value
- 2차원 리스트 & 이중 for loop 익히기
- cycle (itertools 라이브러리)
