n = int(input())

computers = [list(map(int, input().split())) for _ in range(n)]

# queue = []


# def bfs(n):
#     for i in range(n):
#         for j in range(n):
#             if i != j and com[i][j] == 1:
#                 queue.append([i, j])

# def sol():
#     cnt = 0
#     for i in range(len(queue)):
#         for j in range(len(queue)):
#             if j > i and queue[i][1] == queue[j][0] and queue[i][0] == queue[j][1]:
#                 cnt += 1
#     print(n-cnt)

# bfs(n)
# sol()

def dfs(computers, visited, v):
    queue = [v]
    while queue:
        j = queue.pop()  # queue에 저장한 값을 j에 저장 (처음 v값 : 0)
        if visited[j] == 0:
            visited[j] = 1  # 방문한 번째를 1로 바꿈
        for i in range(0, len(computers)):  # len(computers)는 n과 같음
            # 컴퓨터의 네트워크는 양방향이므로 전에 확인한 컴퓨터는 재확인 불필요
            # 그러므로 visited로 전에 확인했는지를 알 수 있음
            if computers[j][i] == 1 and visited[i] == 0:
                queue.append(i)  # dfs함수가 한 턴 끝나기 전까지 비교된 네트워크가 모두 이어져있음


def solution(n, computers):
    ans = 0
    visited = [0] * n  # n만큼 visited에 0을 저장
    v = 0
    while 0 in visited:
        if visited[v] == 0:
            dfs(computers, visited, v)
            ans += 1
        v += 1
    return ans


print(solution(n, computers))
