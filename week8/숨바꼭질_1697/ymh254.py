from collections import deque

n, k = map(int, input().split())


def bfs(n, k):
    visit = [False] * 100001
    cnt = 0
    q = deque([[n, cnt]])
    while q:
        p = q.popleft()
        cnt = p[1]
        if visit[p[0]] == False:
            visit[p[0]] = True
            if p[0] == k:
                return cnt
            else:
                cnt += 1
                if p[0] * 2 < 100001:
                    q.append([p[0]*2, cnt])
                if p[0] + 1 < 100001:
                    q.append([p[0]+1, cnt])
                if p[0] - 1 >= 0:
                    q.append([p[0]-1, cnt])


print(bfs(n, k))
