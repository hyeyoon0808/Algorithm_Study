n, m, v = list(map(int, (input().split())))
# dfs로 방문한 숫자(노드)를 저장(함수안에서 바로 프린트 할 경우 필요 없다)
# visited = []
# 주어진 숫자와 연결된 숫자 확인
visit = [0]*(n+1)
check = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    check[a][b] = 1
    check[b][a] = 1


def dfs(v):
    # visited.append(v)
    visit[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        # visted에 저장되지 않고 해당 숫자와 제일 가까운 숫자를 저장
        # if i not in visited and check[v][i] == 1:
        if visit[i] == 0 and check[v][i] == 1:
            dfs(i)
    # return visited


# print(*dfs(v, visited, check))
dfs(v)
print()


def bfs(v):
    queue = [v]  # 방문해야 할 숫자 저장
    # visit = [v]
    visit[v] = 0  # dfs에서 0을 1로 만들었으므로 다시 0으로 만든다
    while queue:  # 방문해야 할 숫자가 없을때까지!
        v = queue.pop(0)  # 방문해야 할 숫자를 빼낸 후 v에 새로 저장
        print(v, end=' ')
        for i in range(1, n+1):
            # if i not in visit and check[x][i] == 1:
            if visit[i] == 1 and check[v][i] == 1:
                queue.append(i)
                # visit.append(i)
                visit[i] = 0
    # return visit


# print(*bfs(v))
bfs(v)
