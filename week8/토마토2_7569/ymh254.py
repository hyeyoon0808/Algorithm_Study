from collections import deque

m, n, h = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(n)]for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if lst[i][j][k] == 1:
                q.append([i, j, k])

xx = [-1, 0, 1, 0, 0, 0]
yy = [0, -1, 0, 1, 0, 0]
zz = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        l = q.popleft()
        for i in range(6):
            nx = l[2] + xx[i]
            ny = l[1] + yy[i]
            nz = l[0] + zz[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            if lst[nz][ny][nx] == 0:
                lst[nz][ny][nx] = lst[l[0]][l[1]][l[2]] + 1
                q.append([nz, ny, nx])


def ans():
    answer = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if lst[i][j][k] == 0:
                    return -1
                answer = max(answer, lst[i][j][k])
    return answer-1


bfs()
print(ans())
