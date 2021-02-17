import sys
input = sys.stdin.readline
from collections import deque

dx=[0,0,0,0,1,-1]
dy=[0,0,1,-1,0,0]
dz=[1,-1,0,0,0,0]

def bfs(tomato, d, answer):
    count=answer
    while d:
        v=d.popleft()
        count=v[3]
        for i in range(6):
            nx=dx[i]+v[0]   #v[0],v[1],v[2] 순서를 착각함
            ny=dy[i]+v[1]
            nz=dz[i]+v[2]

            if 0<=nx and nx<m and 0<=ny and ny<n and 0<=nz and nz<h:
                if tomato[nz][nx][ny] ==0 and tomato[nz][nx][ny]  != -1:
                    #방문처리
                    tomato[nz][nx][ny] =1
                    d.append([nx, ny, nz, count+1])
    return count

# '-1' 골라내는 작업도 함수로 적용해야 컴파일 에러 안남
def bfsCount(ans, tomato):
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x]==0:
                    return -1
    return ans


m,n,h=map(int, input().split())
tomato=[]
answer=0

for _ in range(h):
    to=[]
    for _ in range(n):
        t=list(map(int, input().split()))
        to.append(t)
    tomato.append(to)

# 시작점 찾기 (변수를 m,n,h로 두면 안됨(변수인지 인식 못함))
d=deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x]==1:
                d.append([z,y,x, answer])

ans=bfs(tomato, d, answer)
print(bfsCount(ans, tomato))
