from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            print(dist[v])
            break
        for nx in (v-1, v+1, v*2):
            if 0 <= nx <= max and not dist[nx]:
                dist[nx] = dist[v]+1    # 트리가 아래로 내려갈 수록 +1
                q.append(nx)


n, k = map(int, input().split())  # n: 수빈위치, k: 동생위치
max = 10**5     # 10의 5제곱근, 시간초과 방지용 but why?
dist = [0]*(max+1)  # 이동하는 거리 저장할 리스트

bfs()


# 토마토 방법으로 하려다 시간초과 ... (사이트에 코드 있음, vscode에선 잘 돌아감)
