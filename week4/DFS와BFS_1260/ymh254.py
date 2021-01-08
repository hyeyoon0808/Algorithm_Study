n, m, v = list(map(int, (input().split())))

num = [[]]
for i in range(m):
    num.append(list(map(int, input().split())))

visited = [False] * len(num)


def dfs(num, visited, x):
    visited[x] = True
    print(x, end=' ')
    for i in num[x]:
        if not visited[i]:
            dfs(num, visited, i)


dfs(num, visited, 1)
