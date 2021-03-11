import sys
input=sys.stdin.readline

count = 0
#앞으로 전진할 수 있는지 확인하는 함수
def solve(i,j):
    global count
    count+=1
    if j == c-1:
        return True
    for d in dx:
        if 0<=i+d<r and grid[i+d][j+1]=="." and not visit[i+d][j+1]:    #범위 벗어나지x, .인지 검사, 방문하지x
            visit[i+d][j+1] = True
            if solve(i+d, j+1): #다음칸에 대해 재귀적으로 함수 호출
                return True
    return False

r, c = map(int, input().split())
grid = [list(input().rstrip("\n")) for _ in range(r)]   #rstrip(): 인자로 전달된 문자를 string의 오른쪽에서 제거함
visit = [[False]*c for _ in range(0,r)]

    
dx = [-1,0,1]   #위(-1), 앞으로(0), 밑으로(1)
ans = 0

for i in range(0,r):
    if grid[i][0] == ".":
        if solve(i,0):
            ans+=1

print(ans)