from collections import deque

m, n, h = map(int, input().split())
ts = [[]for _ in range(h)]
for i in range(h):
    for j in range(n):
        ts[i].append(list(map(int, input().split())))
print(ts)
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if ts[i][j][k] == 1:
                queue.append([i, j, k])

xx = [-1, 1, 0, 0, 0, 0]
yy = [0, 0, -1, 1, 0, 0]
zz = [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        l = queue.popleft()
        for i in range(6):
            dx = l[2] + xx[i]
            dy = l[1] + yy[i]
            dz = l[0] + zz[i]
            if dx < 0 or dx >= m or dy < 0 or dy >= n or dz < 0 or dz >= h:
                continue
            if ts[dz][dy][dx] == 0:
                ts[dz][dy][dx] = ts[l[0]][l[1]][l[2]]+1
                queue.append([dz, dy, dx])


def sol():
    ans = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                a = ts[i][j][k]
                if a == 0:
                    print(-1)
                    return
                ans = max(ans, a)
    print(ans-1)


bfs()
sol()

# 결국 3차원 배열을 만들어서 했다.. (배열안의 배열안의 배열 ex)[[[],[],[]],[[],[],[]]])
# 밑에 껀 왜 틀리지....
# 후.........

# ts = []
# for i in range(h):
#     for j in range(n):
#         ts.append(list(map(int, input().split())))

# queue = deque()
# for y in range(n*h):
#     for x in range(m):
#         if ts[y][x] == 1:
#             queue.append([y, x])

# xx = [-1, 1, 0, 0, 0, 0]
# yy = [0, 0, -1, 1, -n, +n]


# def bfs():
#     while queue:
#         l = queue.popleft()
#         for i in range(6):
#             dy = l[0]+yy[i]
#             dx = l[1]+xx[i]
#             if dx < 0 or dx >= m or dy < 0 or dy >= n*h:
#                 continue
#             if ts[dy][dx] == 0:
#                 ts[dy][dx] = ts[l[0]][l[1]] + 1
#                 queue.append([dy, dx])


# def sol():
#     ans = 0
#     for i in range(n*h):
#         for j in range(m):
#             a = ts[i][j]
#             if a == 0:
#                 print(-1)
#                 return
#             ans = max(ans, a)
#     print(ans-1)


# dfs()
# sol()
