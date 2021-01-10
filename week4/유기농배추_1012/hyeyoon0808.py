# 최단경로문제 -> BFS
def bfs(farm, i, j, M, N, visited):
    
    if farm[i][j] == 0: #0일 경우 함수를 넘김
        visited.append([i, j])
        return [0, visited] 
    
    block = [] #함수 안에서만 쓰일 블록, 붙어있는 배추 그룹을 의미
    queue = [[i, j]] #함수 안에서만 쓰일 큐
    
    while queue:
        [i, j] = queue.pop(0)
        block.append([i, j]) #블록에 쌓아줌
        visited.append([i, j]) #방문 리스트에 쌓아줌
        
        if farm[i][j] == 1: #각각 상하좌우를 확인하는 조건문
            if i < N-1 and farm[i+1][j] == 1 and [i+1, j] not in block and [i+1, j] not in queue:
                queue.append([i+1, j])
            if j < M-1 and farm[i][j+1] == 1 and [i, j+1] not in block and [i, j+1] not in queue:
                queue.append([i, j+1])
            if j > 0 and farm[i][j-1] == 1 and [i, j-1] not in block and [i, j-1] not in queue:
                queue.append([i, j-1])
            if i > 0 and farm[i-1][j] == 1 and [i-1, j] not in block and [i-1, j] not in queue:
                queue.append([i-1, j])

    return [len(block), visited] 


#case 몇번 수행?
case = int(input())

for _ in range(case):
    M, N, K = map(int, input().split())
    
    #농장 형태 리스트화
    farm = [[0 for _ in range(M)] for _ in range(N)]
    
    #배추 있는 공간 표시
    for _ in range(K):
        X, Y = map(int,input().split())
        farm[Y][X] = 1
    
    visited = []
    result = 0
    
    #0,0부터 끝까지 실행
    for i in range(N):
        for j in range(M):
            if [i, j] not in visited:
                [size, visited] = bfs(farm,i,j,M,N,visited)
                if size != 0: #배추가 있는 농가만
                    result += 1 
                    
	#배추 그룹은 몇개?
    print(result)

