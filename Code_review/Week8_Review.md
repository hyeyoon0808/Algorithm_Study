# :pencil: Week8 코드 리뷰

### :round_pushpin: 여행경로_43164

`defaultdict()`

접근하는 키가 존재하지 않는 경우 오류가 아닌 지정해준 데이터 타입의 기본값을 가지는 키를 생성함

- str : `""` (기본값)
- int : `0` 

```python
#str
from collections import defaultdict
a=defaultdict(str)

print(a)    		#defaultdict(<class 'str'>, {})
print(a['t'])   #    (''이기 때문에 아무글자도 나오지 않음)
a['t2']='tt'
print(a)    		#defaultdict(<class 'str'>, {'t': '', 't2': 'tt'})
```

```python
#int
from collections import defaultdict
b=defaultdict(int)

print(b)    		#defaultdict(<class 'int'>, {})
print(b['t'])   #0
b['t2']='tt'
print(b)    		#defaultdict(<class 'int'>, {'t': 0, 't2': 'tt'})
```

```python
#function
from collections import defaultdict
def d():
    return 1

c=defaultdict(d)
print(c['t'])   #1
print(c)    		#defaultdict(<function d at 0x7fa8816baf70>, {'t': 1})
```

