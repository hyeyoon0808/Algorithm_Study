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
                return ans - 1
            for e in arr[k]:
                if visited[e] == False:
                    visited[e] == True
                    q.append(e)
    return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [False] * (n+1)
print(bfs(a))

# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
# xy = []
# for _ in range(m):
#     xy.append(list(map(int, input().split())))
# dic = dict()
# for x, y in xy:
#     if x in dic:
#         dic[x].append(y)
#     else:
#         dic[x] = [y]
# v = max(a, b)
# cnt = 1
# for i in dic.items():
#     if v in i[1]:
#         v = i[0]
