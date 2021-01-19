#bfs
from collections import deque
import sys
input sys.stdin.readline

m, n = map(int, input().split())
arr = []
deq = deque()
visit = [[0 for i in range(m)] for j in range(n)]

for i range(n):
    # graph.append(list(map(int, input().split())))
    arr.append([*map(int, input().split())]) # => list대신 쓸수 있다
    # * -> positional arguments만 받음 ('apple')
    # ** -> keyword arguments 받음 (first='apple')

for i in range(n):  
    for j in range(m):
        if arr[i][j] == 1: #익은 토마토 체크
            deq.append((i, j))
            visit[i][j] = 1

# 전체 배열에서 안익은 토마토가 있는지 확인
flag = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flag = 0
            break
# 처음부터 모든 토마토가 익은 상태는 0
if flag and deq:
    pring(0)
    exit(0)

# 모든 토마토가 익지 않았을때 하루를 카운트하며 bfs 수행
# 단, 익은 토마토 기준으로
d_x = [0, 0, 1, -1] 
d_y = [1, -1, 0, 0] 
ans = 0 

while 1: 
    deq_second = deque() 
    while deq: 
        x, y = deq.popleft() 
        for i in range(4): 
            new_x = x + d_x[i] 
            new_y = y + d_y[i] 
            if not(0 <= new_x < n and 0 <= new_y < m): continue 
            if visit[new_x][new_y] or arr[new_x][new_y] != 0: continue 
            deq_second.append((new_x, new_y)) 
            visit[new_x][new_y] = 1 
            arr[new_x][new_y] = 1 
    deq = deq_second 
    if not deq: break 
    ans += 1 
    
#아직 익지 않은 토마토가 있는지 확인 
for i in range(n): 
    if 0 in arr[i]: 
        print(-1) 
        exit(0)
        
print(ans)



