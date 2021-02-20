# tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
#     "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

# def solution(tickets):
#     ans = ["ICN"]
#     while tickets:
#         lst = []
#         for i in range(len(tickets)):
#             if len(tickets) == 0:
#                 break
#             if ans[-1] == tickets[i][0]:
#                 lst.append(tickets[i])
#                 lst.sort(key=lambda x: x[1])
#         ans.append(lst[0][1])
#         tickets.remove(lst[0])
#     return ans

# 위의 코드를 실행했을 때 캐이스 1, 2번이 오류나는 이유:
# tickets = [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]과 같은 예제 때문
# 이 때문에 아래 코드처럼 시작점으로 묶은 뒤 if start not in dic or len(dic[start]) == 0와 같은 조건으로
# 도착점이 시작점이 될 수 없는 경우를 생각해줘야 함


def solution(tickets):
    dic = dict()
    lst = ['ICN']
    ans = []
    for i, j in tickets:
        if i in dic:
            dic[i].append(j)
        else:
            dic[i] = [j]
    for i in dic.keys():
        dic[i].sort(reverse=True)
    while len(ans) <= len(tickets):
        start = lst[-1]
        if start not in dic or len(dic[start]) == 0:
            ans.append(lst.pop())
        else:
            lst.append(dic[start].pop())
    return ans[::-1]


print(solution(tickets))
