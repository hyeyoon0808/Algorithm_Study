n = int(input())
m = int(input())
check = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    check[a][b] = 1
    check[b][a] = 1


def bfs(v):
    queue = [v]
    visit = [v]
    while queue:
        v = queue.pop(0)
        for i in range(1, n+1):
            if check[v][i] == 1 and i not in visit:
                queue.append(i)
                visit.append(i)
    return(visit)


print(len(bfs(1))-1)
