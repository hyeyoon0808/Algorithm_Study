from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    ans = 0
    while q:
        ans += 1
        for _ in range(len(q)):
            k = q.popleft()
            if k == b:
                return ans-1
            for i in arr[k]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
    return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    # 한 숫자에 연결된 숫자를 모두 확인하기 위함
    arr[x].append(y)
    arr[y].append(x)
visited = [False] * (n+1)
print(bfs(a))
