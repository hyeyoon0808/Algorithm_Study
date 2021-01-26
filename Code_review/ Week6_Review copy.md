# :pencil: Week4 코드 리뷰

### :round_pushpin: 덩치_7568

- print(*[리스트명]) : 한 칸씩 뛰어서 한 줄에 출력



### :round_pushpin: 단어 변환_43163

- global : 변수 앞에 선언하여 전역 변수로 사용가능케 함

- Zip 내장 함수

  : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수

  ```python
  Number=[1,2,3,4]
  Name=['hong', 'gil', 'dong', 'nim']
  dic={}
  
  for num, name in zip(Number, Name):
    dic[number]=name
  
  print(dic)	# {1: 'hong', 2:'gil', 3:'dong', 4:'nim'}
  ```

  <br/>

  - 글자 비교 가능 

  ```python
  a='hit'
  b='hot'
  
  for x,y in zip(a,b):
    if x != y:
      print('다르다')
    else: 
      print('같다')
      	
  # '다르다' if x!=y else '같다' 
        
  # 같다		#('h', 'h')
  # 다르다		#('i', 'o')
  # 같다 		#('t', 't')
  ```

  

  > **알파벳이 하나만 다른 단어를 찾기 위해 사용한다면?**
  >
  > > transistable=lambda a,b: sum((1 if x!=y else 0) for x,y in zip(a,b))==1
  > >
  > > : a와 b를 zip을 이용하여 각 알파벳을 비교
  > >
  > > -> 각 알파벳이 비교될 때 두개가 다르다면 1, 같으면 0을 받아 더한다.
  > >
  > > -> 더한값이 1이여만 하나만 다른 단어임을 알 수 있음(==1) -> true일때만 리턴

  

### :round_pushpin: 단어 수학_1339

- dict 일때

```python
alpha = {'a': 10000, 'c': 1010, 'd': 100, 'e': 10, 'b': 1, 'g': 100, 'f': 1}

#key로 비교하고 싶을때1 (key만 다시 담을 때)
print(sorted(alpha, key=lambda x: x[0], reverse=True))	# ['g', 'f', 'e', 'd', 'c', 'b', 'a']

#key 비교2(value함께 담을 때 )
print(sorted(alpha.items(), key=lambda x: x[0], reverse=True))	# [('g', 100), ('f', 1), ('e', 10), ('d', 100), ('c', 1010), ('b', 1), ('a', 10000)]

#value로 비교하고 싶을때 
print(sorted(alpha.items(), key=lambda x: x[1], reverse=True))	# [('a', 10000), ('c', 1010), ('d', 100), ('g', 100), ('e', 10), ('b', 1), ('f', 1)]
```