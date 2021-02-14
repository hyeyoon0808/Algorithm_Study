def solution(tickets):
    answer = []
    # 도착 순으로 경로 딕셔너리 생성
    routes = dict()
    for t in tickets:
        if t[0] in routes:
            routes[t[0]].append(t[1])
        else:
            routes[t[0]] = [t[1]]
    #print(routes)
    
    #key 값마다 value를 역순으로 정렬
    for k in routes.keys():
        routes[k].sort(reverse=True)

    #1번째 출발지는 "ICN"으로 고정    
    start=["ICN"]
    answer = []
    while start:
        stack = start[-1]
        # answer에 담겨질 때는 start에 값이 꽉차고 routes에 값이 없을 때이므로 
        # answer에는 반대로 값이 들어가 있음
        if stack not in routes or len(routes[stack]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[stack].pop())
    #처음부터 끝까지 -1칸 간격으로 (역순)
    return answer[::-1]