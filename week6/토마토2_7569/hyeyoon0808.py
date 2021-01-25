from _collections import deque

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]  # 아래층 윗층 앞 뒤 좌 우


# BFS로 주변 토마토 익히기
def ripen():
    while q:
        x, y, z = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < H and 0 <= ny < M and 0 <= nz < N:
                if box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = box[x][y][z] + 1
                    q.append((nx, ny, nz))


# 0이 있을 경우 토마토는 다 익지 못함, 0이 없으면 day를 return
def check_ripen():
    max_day = 0
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if box[i][j][k] == 0:
                    return -1
                else:
                    max_day = max(max_day, box[i][j][k])

    return max_day - 1

N, M, H = map(int, input().split())

# 토마토 상자 채우기
box = []
for i in range(H):
    step = [list(map(int, input().split())) for _ in range(M)]
    box.append(step)


# 익은 토마토 찾기
q = deque()
for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k] == 1:
                q.append((i, j, k))


ripen()
answer = check_ripen()
print(answer)