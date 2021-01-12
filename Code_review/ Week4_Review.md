# :pencil: Week4 코드 리뷰

### :round_pushpin: ATM_11399

- 



### :round_pushpin: 회의실배정_1931

- meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
  1. x[1]을 기준으로 sort
  2. x[1]을 sort한 기준으로 x[1]에서 같은 경우에만 x[0]자리 비교 후 sort
- ab.sort(key=lambda x: x[0])
  - 뒤에 요소만 소팅해주면 끝나는 시간이 같은 경우 시작시간을 고려하지 않고 소팅하므로 앞에요소를 먼저 소팅해줘야함
- ab.sort(key=lambda x: x[1]) : lambda는 함수를 한줄로 만드는 형식으로 형태는 'lambda 인자 : 표현식'
  - 밑 정렬에서는 x[1]이 정렬된 후에 x[1]이 같은 경우 x[0]을 sort해주는 듯!!



### :round_pushpin: DFS와BFS_1260

- graph = [[] for _ in range(n+1)]
  - 빈 이차열 리스트 만들기
- from collections import deque
  - queue를 쓸때, list보다 시간복잡도에서 유리
- DFS: 경로의 특징을 저장해둬야 하는 문제
  - ex) 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안 된다는 문제 등, 각각의 경로마다 특징을 저장해둬야 할 때
  - 검색 대상 그래프가 정말 크다면 DFS
- BFS: 최단거리 구하는 문제
  - ex) 미로찾기 등 최단거리를 구해야 할 경우
  - 검색 대상의 규모가 크지 않고, 검색 시작 지점으로부터 원하는 대상이 별로 멀지 않다면 BFS



### :round_pushpin:  유기농배추_1012

- 상하좌우 문제에서 유용한 것

```python
# 현재 노드 기준으로 상하좌우 좌표(x, y) 값
xx = [-1, 0, 1, 0]
yy = [0, 1, 0, -1]

for i in range(4):
        nx = x+xx[i]
        ny = y+yy[i]
```



### :round_pushpin:  타겟넘버_1012

- **product - from itertools import product**
  - 알아서 원소의 모든 요소의 조합을 구하는 라이브러리