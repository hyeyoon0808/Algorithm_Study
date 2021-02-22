import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    d=deque([n])
    while d:
        v=d.popleft()
        if v==k:
            print(count[v]) 
            break   
        for i in (v-1, v+1, v*2):
            if 0<=i<=max and count[i]==0:   #i의 범위 : max보다 작거나 같음 (같음 주의-)
                count[i]=count[v]+1     #트리위치에서 아래로 내려갈수록 플러스 일
                d.append(i)


n,k=map(int, input().split())
max=10**5    #시간방지용
count=[0]*(max+1)   #max보다 하나 크게 설정할 것(런타임 에러 방지)   
bfs()
