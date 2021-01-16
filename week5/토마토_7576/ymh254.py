from collections import deque
m, n = list(map(int, input().split()))
t = [list(map(int, input().split())) for _ in range(n)]

xx = [-1, 1, 0, 0]
yy = [0, 0, -1, 1]
# 리스트를 deque로 해주면 popleft, popright 등 다양하게 구현가능.
queue = deque()

for i in range(n):
    for j in range(m):
        if t[i][j] == 1:
            # 1이 있는 칸의 위치를 queue에 저장
            queue.append([i, j])


def bfs():
    global queue
    while queue:
        l = queue.popleft()  # queue에 담긴 첫번째 1의 위치를 l에 저장
        for i in range(4):
            # 상하좌우 확인
            nx = l[1]+xx[i]
            ny = l[0]+yy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if t[ny][nx] == 0:  # 상하좌우에 0이 있을 시 비교하는 위치의 값 +1을 해줌 (하루가 지남을 의미)
                # if 0 <= nx < m and 0 <= ny < n and t[ny][nx] == 0:
                t[ny][nx] = t[l[0]][l[1]]+1
                queue.append([ny, nx])


def sol():
    lst = []
    ans = 0
    for i in range(n):
        for j in range(m):
            a = t[i][j]
            # if t[i][j] == 0:
            # a가 0이 있다는 것은 토마토가 익지 못하는 상황
            if a == 0:
                print(-1)
                return
            # for문에 돌면서 갱신되는 a값을 ans에 저장하면서 전 a값(ans)과 현 a값을 비교하여 큰 값을 바로 ans에 저장.
            ans = max(ans, a)
            # t의 모든 값을 배열에 담아서 max를 구하니까 시간초과 남.
            # else:
            #     lst.append(t[i][j])
            # ans = max(lst)
    print(ans-1)  # 시발점이 1이므로 -1을 해줘야 정확한 날짜 출력


bfs()
sol()
