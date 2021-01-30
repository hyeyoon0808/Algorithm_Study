tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]

# lst = []
# ans = [tickets[0][0]]

# for i in range(len(tickets)):
#     if 'ICN' in tickets[i]:
#         lst.append(tickets[i])
#     else:
#         break
# lst = sorted(lst, key=lambda x: x[1])
# d = lst[0]

# for _ in range(len(tickets)):
#     ans.append(d[1])
#     tickets.remove(d)
#     lst = []
#     for i in range(len(tickets)):
#         if d[1] == tickets[i][0]:
#             if tickets[i] in lst:
#                 break
#             lst.append(tickets[i])
#     if len(lst) == 0:
#         break
#     lst = sorted(lst, key=lambda x: x[1], reverse=True)
#     lst = [lst[-1]]
#     d = lst[0]
# print(ans)

d = dict()

for i in tickets:
    if i[0] in d:
        d[i[0]].append(i[1])
    else:
        # 처음 d에 {i[0] : i[1]}을 추가할 때 i[1]를 리스트로 저장해야 i[0] 중복시 append가 됨
        d[i[0]] = [i[1]]

for i in d.keys():
    d[i].sort(reverse=True)
print(d)
lst = ['ICN']
ans = []
while lst:
    # 아래코드는 런타임 에러..
    # while len(lst) != len(tickets)+1:
    # start = lst[-1]
    # lst.append(d[start].pop())

    start = lst[-1]
    # start not in d를 안해주면 마지막 도착지점이 출발지점에 없을 시 에러남
    if start not in d or len(d[start]) == 0:
        ans.append(lst.pop())
    else:
        lst.append(d[start].pop())
print(ans[::-1])
