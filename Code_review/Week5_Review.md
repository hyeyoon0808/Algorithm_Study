# :pencil: Week5 코드 리뷰

### :round_pushpin: 토마토 - 7576

- `while 1:`  = `while true:`

- arr.append(list(map(int, input().split()))) 대신,

  ->  **arr.append([*map(int, input().split())])** 로 사용 가능

  - \* : positional arguments만 받음 ('apple')
  - ** : keyword arguments 받음 (first='apple')

- pop사용법
  - list : pop()
  - deque : popleft()
  - stack : popright()



### :round_pushpin:숨바꼭질 - 1697

`dist = [0]*100001`

- 10의 5제곱근 = 10**5

- 리스트를 위와 방식대로 만들어두면, **시간초과 방지용** 

  \*빈리스트에 추가하는 건 인덱스와 값을 찾아야 해서 두번 돌아가는 형식이라 시간초과가 날 수 있음.



### :round_pushpin: 수정렬3 - 10989

- 메모리 제한 문제로 모든 수를 리스트에 저장하고 정렬하면 안됨 -> 카운팅(계수 정렬) 필요
  - 계수 정렬 : 값을 저장하지 않고 동일한 인덱스에 카운트해준 뒤 그 정보만 프린트



### :round_pushpin: 시리얼번호 - 1431

- 문자열에서 숫자찾기
  - isdecimal()  : 단일 글자가 '숫자' 모양으로 생겼으면 무조건 True를 반환하는 함수  (즉, 숫자처럼 생긴 '모든 글자'를 숫자로 침) 
  - isdigit()  : 주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수이기 때문에 특정 문자 중 숫자모양 글자를 숫자로 치지않음 
  - isnumeric()  : 숫자값 표현에 해당하는 문자열까지 인정   (제곱근 및 분수, 거듭제곱 특수문자도 isnumeric() 함수는 True를 반환)
- 문자열에서 알파벳 구성 여부 확인 `.isalpha()`

- .strip() : 양쪽 공백 지우기 `input().strip()`

- **import re**
  `re.findall("\d", string) ` : 문자열에서 숫자뽑아내기
  - "\d+" >> 숫자 **묶음** 단위별 추출
  - "\d"  >> 한자리 숫자 단위별로 추출

- `if i >= '0' and i <= '9':` (파이썬에서만 가능한 문법) -> 0~9까지 