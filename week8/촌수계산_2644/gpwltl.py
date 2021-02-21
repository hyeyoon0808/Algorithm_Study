import sys
input = sys.stdin.readline
from collections import deque

def bfs(people, start, visited):
    d=deque([start])
    visited[start]=True
    count=0
    
    while d:
        count+=1
        for _ in range(len(d)):  #연결된 불필요한 선 카운트세지 않기 위해서 (이부분 또 적용못함...)
            v=d.popleft()
            for i in people[v]:
                if not visited[i]:
                    
                    if i==b:
                        return count
                        break

                    else: 
                        d.append(i)
                        visited[i]=True
    
    return -1


m=int(input())
a,b=map(int, input().split())
n=int(input())

people=[[] for _ in range(m+1)]
visited=[False]*(m+1)

for _ in range(n):
    x,y=map(int, input().split())
    people[x].append(y)
    people[y].append(x)

if a==b: 
    print(0)
else: 
    print(bfs(people, a, visited))