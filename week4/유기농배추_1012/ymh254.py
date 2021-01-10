import sys
sys.setrecursionlimit(10000)

xx = [-1, 0, 1, 0]
yy = [0, 1, 0, -1]
cnt = 0


def dfs(x, y):
    p[x][y] = 0
    for i in range(4):
        nx = x+xx[i]
        ny = y+yy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if p[nx][ny] == 1:
            dfs(nx, ny)


def ans():
    cnt = 0
    for i in range(m):
        for j in range(n):
            if p[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)


t = int(input())
for _ in range(t):
    m, n, k = list(map(int, input().split()))

    p = [[0]*n for _ in range(m)]
    for _ in range(k):
        a, b = list(map(int, input().split()))
        p[a][b] = 1

    ans()
