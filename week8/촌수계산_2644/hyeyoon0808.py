N=int(input())
a,b=map(int,input().split())
m=int(input())

relation = [[]for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(m):
    c,d = map(int, input().split())
    relation[c].append(d)
    relation[d].append(c)

answer = 0
re=relation[a]
while True:
    temp=[]
    for i in re:
        for j in relation[i]:
            if visited[j]==0:
                visited[j]=1
                temp.append(j)
    answer+=1
    if b in temp:
        find=True
        break
    if len(temp)==0:
        find=False
        break
    re = temp
if find:
    print(answer+1)
else:
    print(-1)