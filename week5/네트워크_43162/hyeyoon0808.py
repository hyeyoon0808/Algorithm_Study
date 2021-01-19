def solution(n, computers):
    # dfs를 통해 모든 점을 방문하고 네트워크의 개수 새서 리턴
    def dfs(s):
        ch[s]=1
        for i in a[s]:
            if ch[i] == 0:
                dfs(i)

    a=[[] for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            if computers[i][j] == 1:
                a[i].append(j)
                a[j].append(i)
    ch=[0]*n
    c=0
    for i in range(n):
        if ch[i]==0:
            c+=1
            dfs(i)
    return c