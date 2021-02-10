import sys
input=sys.stdin.readline
from collections import deque

def bfs(family, start, visited):
    count=0
    queue=deque([start])
    visited[start]=True
    while queue:
        count+=1
        for _ in range(len(queue)): #이 부분 추가해야 함! -> 연결된 불필요한 선 카운트세지 않기 위해서 
            v=queue.popleft()
            for i in family[v]:
                if not visited[i]:
                    if i==b:
                        return count
                        break
                    else:
                        queue.append(i)
                        visited[i]=True

    return -1   # '두 사람의 친척 관계가 전혀 없어' 조건 충족

n=int(input())
a,b=map(int, input().split())
m=int(input())


family=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    x,y=map(int, input().split())
    family[x].append(y)
    family[y].append(x)

if a==b:    #자기 자신은 0촌
    print(0)
else: 
    print(bfs(family, a, visited))