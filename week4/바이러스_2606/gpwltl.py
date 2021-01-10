from collections import deque
import sys
input = sys.stdin.readline

n = int(input())  # 노드 수
m = int(input())  # 간선 수

graph = [[] for _ in range(n+1)]
for i in range(m):  # 범위는 간선수만큼!! why
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

visited = [False]*(n+1)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    answer = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True   # 방문한 노드 True로 바꾸면서,
                answer += 1         # +1 카운트해서 방문한 노드 수 구하기
    print(answer)


bfs(graph, 1, visited)
