import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)  # 재귀제한높이설정


# 이동을 위한 리스트(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(land, x, y):
    land[x][y] = 2  # 방문 처리

    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if land[nx][ny] == 1:   # 옆에가 1(배추o)이면 방문 처리
                land[nx][ny] = 2
                dfs(land, nx, ny)


# 배추있는 곳(1) 찾아서 dfs 실행하고, 묶인 그룹 카운트 +1
def dfsAll(land):
    answer = 0
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                answer += 1
                dfs(land, i, j)
    return answer


testcase = int(input())
for _ in range(testcase):
    m, n, k = map(int, input().split())  # m: 가로, n: 세로, k: 배추o
    land = [[0]*m for _ in range(n)]  # 재배 땅(graph)
    for _ in range(k):
        a, b = map(int, input().split())
        land[b][a] = 1

    print(dfsAll(land))

# 생각 못한 부분 ...!!
# 테이블을 만들 때 계속 두개를 만들어서 비교하려고 했음 ... >> 그냥 하나에 숫자를 부여하는 것이 효율적. (배추x: 0, 배추o: 1, 방문했을 때:2)
