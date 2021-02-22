from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
lst = [[]for _ in range(n+1)]
visit = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)


# return 값을 다르게 하기위해 함수사용
def bfs():
    cnt = 0
    q = deque([b])
    while q:
        cnt += 1
        for _ in range(len(q)):
            l = q.popleft()
            if l == a:
                return cnt-1  # 처음 시작시 더해진 1 빼기
            for j in lst[l]:
                if visit[j] == False:
                    visit[j] = True
                    q.append(j)
    return -1


print(bfs())
