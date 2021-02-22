# 접근하는 키가 존재하지 않는 경우 오류가 아닌 지정해준 데이터 타입의 기본값을 가지는 키를 생성
# str 적어줄 경우 기본값을 "
# int 적어줄 경우 0 호출
from collections import defaultdict


def solution(tickets):
    answer = []
    adj = defaultdict(list)

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    for key in adj.keys():
        adj[key].sort(reverse=True)

    q = ['ICN']
    while q:
        tmp = q[-1]

        if not adj[tmp]:
            answer.append(q.pop())
        else:
            q.append(adj[tmp].pop())
    answer.reverse()
    return answer