record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

#시간초과 ..
# def solution1(record):
#     answer=[]
#     userList=[]

#     #유저리스트 저장
#     for i in record:
#         if i.split()[0]=='Enter':
#             if any(i.split()[1] in sublist for sublist in userList):    #any: list of lists에서 원하는 값 찾기
#                 for user in userList:
#                     if i.split()[1]==user[0]:
#                         user[1]=i.split()[2]
#             else:
#                 userList.append([i.split()[1], i.split()[2]])
                
#         if i.split()[0]=='Change':
#             for user in userList:
#                 if i.split()[1]==user[0]:
#                     user[1]=i.split()[2]


#     #채팅방
#     for i in record:
#         if i.split()[0]=='Enter':
#             for user in userList:
#                 if i.split()[1]==user[0]:
#                     answer.append(user[1]+'님이 들어왔습니다.')

#         if i.split()[0]=='Leave':
#             for user in userList:
#                 if i.split()[1]==user[0]:
#                     answer.append(user[1]+'님이 나갔습니다.')
    
#     return answer


def solution(record):
    answer=[]
    logList=[]
    userList=dict()

    for i in record:
        if i.split()[0]=='Leave':
            logList.append([i.split()[1], "님이 나갔습니다."])
        
        elif i.split()[0]=='Enter':
            logList.append([i.split()[1], "님이 들어왔습니다."])
            userList[i.split()[1]]=i.split()[2]

        elif i.split()[0]=='Change':
            userList[i.split()[1]]=i.split()[2]

    for log in logList:
        answer.append(userList[log[0]]+log[1])
    
    return answer


print(solution(record))