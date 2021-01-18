n,k = map(int,input().split()) 
que = [] 
v_que = [ 0 for _ in range(100001)] 
# 방문한 곳의 depth를 기록
depth = [] 
depth.append(0) 
que.append(n) 
while True: 
    x = que.pop(0) 
    xc = depth.pop(0) 
    
    # 방문하지 않았던 곳이면 실행. 
    if v_que[x] != 1: 
        v_que[x] = 1 
        
        if x-1 >= 0: 
            que.append(x-1) 
            # 현재 depth + 1 
            depth.append(xc + 1) 
        if 2*x <= 100000 : 
            que.append(2*x) 
            depth.append(xc + 1) 
        if x+1 <= 100000 : 
            que.append(x+1) 
            depth.append(xc + 1) 
    if x == k: 
        print(xc) 
        break

