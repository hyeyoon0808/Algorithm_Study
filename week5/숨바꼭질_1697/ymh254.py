from collections import deque

n, k = map(int, input().split())
f = [False] * 100001  # 0 <= n <= 100000까지의 범위를 모두 False 설정


def bfs(n):
    cnt = 0
    queue = deque([[n, cnt]])  # n(수빈이 좌표)와 cnt를 담은 list를 deque에 저장
    while queue:
        m = queue.popleft()
        n = m[0]
        cnt = m[1]
        if not f[n]:
            f[n] = True  # 중복을 없애기위해[?] False인 지점을 방분하면 True로 바꿈
            if n == k:
                return cnt
            cnt += 1
            # 모든 경우를 queue에 저장하여 경우를 구한다
            if (n*2) <= 100000:
                queue.append([n*2, cnt])
            if (n+1) <= 100000:
                queue.append([n+1, cnt])
            if (n-1) >= 0:
                queue.append([n-1, cnt])
    return cnt  # 제일 처음, 즉 최저 이동 수를 return


print(bfs(n))
