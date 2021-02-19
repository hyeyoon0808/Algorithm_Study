import sys
sys.setrecursionlimit(10000)  # 최대 재귀한도 깊이 설정(런타임에러 방지)

xx = [-1, 0, 1, 0]
yy = [0, -1, 0, 1]


def dfs(x, y):
    arr[y][x] = 0
    for i in range(4):
        nx = x + xx[i]
        ny = y + yy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if arr[ny][nx] == 1:
            dfs(nx, ny)


def ans():
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[j][i] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    ans()
