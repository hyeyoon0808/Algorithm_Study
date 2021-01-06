# 문제풀이 / 문제리뷰

1. 
```python
for i in range(0, leng):  # leng대신 (1, leng+1)쓰면 런타임에러남!
    ans += int(nums[i])
```
=> 리스트의 첫번째 인덱스 값은 0부터!!!

- 변수 쓰기 전에 위에서 무조건 변수 선언!!
