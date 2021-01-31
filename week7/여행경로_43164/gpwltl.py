
def dfs(answer, stack, start, visited):
    for i in range(len(tickets)):
        if start==tickets[i][0] and visited[i]==False:  #도착지 찾아서 stack에 넣어주기 (방문하지 않은 곳 중에서)
            stack.append(tickets[i][1])
            visited[i]=True
            dfs(answer, stack, tickets[i][1], visited)

    answer.append(start)    #더이상 갈 곳없을 때 answer에 넣어주기



def solution(tickets):
    answer=[]
    stack=['ICN']
    visited=[False]*len(tickets)
    tickets.sort()  #먼저 작은 순서대로 배열을 해주고 진행하면 뒤에서 작업 필요없음

    dfs(answer, stack, 'ICN', visited)
    answer.reverse()    #마지막 방문곳부터 넣어주어서 뒤집기
    return answer

