from collections import deque
import sys
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

# 빈 이차열 리스트 만들기(암기!!) -> 크기는 맨 앞자리 남겨두기위해 +1
graph = [[] for _ in range(n+1)]

# 각 번호에 인접한 노드들로 구성한 리스트 생성(이것도 암기!!!)
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

# 인접하는 노드들을 오름차순으로 정렬 -> '여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문' 조건 존재
for i in range(n+1):
    graph[i].sort()

visited = [False]*(n+1)
dfs(graph, v, visited)
print()
visited1 = [False]*(n+1)
bfs(graph, v, visited1)
