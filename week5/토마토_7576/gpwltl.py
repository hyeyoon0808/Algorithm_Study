from collections import deque
import sys
input = sys.stdin.readline


def bfs(queue, answer):
    count = answer
    while queue:
        v = queue.popleft()
        count = v[2]    # v를 중심으로 주변값을 queue에 넣어줄 땐 v에서 +1을 해서 주변값들은 count가 동일
        for i in range(4):
            nx = dx[i]+v[0]
            ny = dy[i]+v[1]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 0 and graph[nx][ny] != -1:
                    graph[nx][ny] = 1
                    queue.append([nx, ny, count+1])
    return count


def bfsCount(answer, graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:  # 0이 존재하면 모두가 익지 못해서 -1 리턴
                return -1
    return answer


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m, n = map(int, input().split())
graph = []
answer = 0      # 최소 날짜
q = deque([])  # deque 이용해서 큐 사용
for i in range(n):  # graph(tomato) 생성
    g = list(map(int, input().split()))
    graph.append(g)

for i in range(n):  # 시작점 찾기
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j, answer])

# 처음에 익은 토마토가 한군데만이 아니라 다른데도 있을시에 동시에 큐에 넣어줌으로써 동시에 서로 다른 토마토가 다른 위치에서 익히도록 해서 answer라는 일수를 계산
answer = bfs(q, answer)

print(bfsCount(answer, graph))
