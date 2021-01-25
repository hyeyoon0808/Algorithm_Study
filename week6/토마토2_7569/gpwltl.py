from collections import deque
import sys
input = sys.stdin.readline


def bfs(q, answer):
    count = answer  # ?
    while q:
        v = q.popleft()
        count = v[3]
        for i in range(6):
            nx = dx[i]+v[0]
            ny = dy[i]+v[1]
            nz = dz[i]+v[2]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and nz >= 0 and nz < h:
                if tomato[nz][nx][ny] == 0 and tomato[nz][nx][ny] != -1:
                    tomato[nz][nx][ny] = 1
                    q.append([nx, ny, nz, count+1])

    return count


def bfsCount(answer, tomato):
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 0:
                    return -1
    return answer


m, n, h = map(int, input().split())  # m: 가로, n: 세로, h: 상자수
tomato = []

# 3차원 배열 만들기
for _ in range(h):
    t = []
    for _ in range(n):
        t.append(list(map(int, input().split())))
    tomato.append(t)


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
answer = 0

# 시작점 찾기
q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                q.append([i, j, k, answer])

ans = bfs(q, answer)
print(bfsCount(ans, tomato))


# 3차원 배열
# a = [[[1, 2], [3, 4]], [5, 6], [7, 8]]
# print(a[0][1][1]) #-> 결과 : 4 (높이, 가로, 세로순)
