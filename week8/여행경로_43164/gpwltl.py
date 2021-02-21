# tickets=[["ICN", "SFO"], ["ICN", 'ATL'], ["SFO", "ATL"], ['ATL', 'ICN'], ['ATL',"SFO"]]
tickets=[["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
# tickets=[["ICN", "A"], ["ICN", "A"], ["A", "ICN"],["A" , "C"]]

def dfs(tickets, visited, start, s, answer):
    for i in range(len(tickets)):
        if tickets[i][0]==start and not visited[i]:
            s.append(tickets[i][1])
            visited[i]=True     #방문처리 항상 생각!!! 
            dfs(tickets, visited, tickets[i][1], s, answer)

    answer.append(start)    #더 이상 가는 곳이 없는 것부터 넣어줘야 
    return answer


def solution(tickets):
    tickets.sort()
    visited=[False]*len(tickets)
    s=[]
    answer=[]

    dfs(tickets, visited, 'ICN', s, answer)
    answer.reverse()
    print(answer)


solution(tickets)    
