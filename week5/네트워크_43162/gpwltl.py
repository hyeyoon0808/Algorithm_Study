n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)

    # 새로운 graph를 만들어줌. 해당 번호에 맞는 인접한 노드들로 구성한 리스트 -> [[], [2], [1,3], [2]]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i+1].append(j+1)

    for i in range(1, n+1):
        if visited[i] == False:
            answer += 1
            dfs(graph, i, visited)
    return answer


print(solution(n, computers))
