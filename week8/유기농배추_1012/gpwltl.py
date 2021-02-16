import sys
input= sys.stdin.readline
sys.setrecursionlimit(50000)  # 재귀제한높이설정 - 런타임에러 방지

#상하좌우
dx=[0,0,1,-1]
dy=[1,-1,0,0]

#카운트 담을 배열
answer=[]

def dfs(baechu, i, j):
    #방문한 배추는 2로 바꿔줘서 방문 처리 
    baechu[i][j]=2

    for p in range(4):
        nx=dx[p]+i
        ny=dy[p]+j

        if 0<=nx and nx<n and 0<=ny and ny<m:
            if baechu[nx][ny]==1:
                baechu[nx][ny]==2
                dfs(baechu, nx, ny)

def dfscount(baechu):
    count=0

    #시작점 찾기
    for i in range(n):
        for j in range(m):
            if baechu[i][j]==1:
                count+=1
                dfs(baechu, i, j)

    return count


testcase=int(input())
for _ in range(testcase):
    m, n, k = map(int, input().split())
    baechu=[[0]*m for _ in range(n)]
    
    #배추판 만들어주기 
    for _ in range(k):
        x,y=map(int, input().split())
        baechu[y][x]=1

    print(dfscount(baechu))



## 여전히 모르거나 인지하지 못한 부분
# 방문처리를 그래프를 만들어서 하려고 했음...그냥 숫자를 늘리면 될 것을 .. 멍청.. 
# 재귀제한설정? 저거 대체 언제는 해야하고 언제는 안해도되는지 의문..