import sys
sys.setrecursionlimit(10000)
# 현재 노드 기준으로 상하좌우 좌표(x, y) 값
xx = [-1, 0, 1, 0]
yy = [0, 1, 0, -1]
cnt = 0


def dfs(x, y):
    p[x][y] = 0
    for i in range(4):
        nx = x+xx[i]
        ny = y+yy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:  # x, y값이 0 또는 밭의 최대길이보다 클 경우를 제외
            continue
        if p[nx][ny] == 1:  # 상하좌우비교 하여 심어져 있을 경우를 찾는다
            dfs(nx, ny)


def ans():
    cnt = 0
    for i in range(m):
        for j in range(n):
            if p[i][j] == 1:  # 배추가 심어져 있을 경우 주변 값을 확인 하기 위해 함수호출
                dfs(i, j)
                cnt += 1  # dfs함수 재귀가 끝나고 포문이 다시 실행 될때마다 count 해줌
    print(cnt)


t = int(input())
for _ in range(t):
    m, n, k = list(map(int, input().split()))

    p = [[0]*n for _ in range(m)]
    for _ in range(k):
        a, b = list(map(int, input().split()))
        p[a][b] = 1

    ans()
