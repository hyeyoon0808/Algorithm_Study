from collections import deque 
def bfs(s): 
    q = deque() 
    visited = [0 for _ in range(n+1)] 
    
    q.append(s) 
    visited[s] = 1 
    
    while q: 
        x = q.popleft() 
        for i in tree[x]: 
            if visited[i] == 0: 
                visited[i] = 1 
                result[i] = result[x] + 1 
                q.append(i) 

n = int(input()) 
a, b = map(int, input().split()) 
m = int(input()) 
tree = [[] for _ in range(n+1)] 
result = [0 for _ in range(n+1)] 

for _ in range(m): 
    x, y = map(int, input().split()) 
    tree[x].append(y) 
    tree[y].append(x) 

bfs(a) 
if result[b] != 0: 
    print(result[b]) 
else: 
    print(-1)

