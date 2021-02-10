record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
# lst = []
# ans = []
# for i in range(len(record)):
#     lst.append(list(record[i].split(" ")))

# for i in range(len(record)-1, -1, -1):
#     for j in range(len(record)):
#         if lst[i][0] == 'Enter' and lst[j][0] == 'Enter' or lst[i][0] == 'Change':
#             if lst[i][1] == lst[j][1] and i != j:
#                 del lst[j][2]
#                 lst[j].append(lst[i][2])
# # print(lst)

# for i in range(len(record)):
#     if lst[i][0] == "Enter":
#         ans.append("{0}님이 들어왔습니다." .format(lst[i][2]))
#     elif lst[i][0] == "Leave":
#         for j in range(i):
#             if lst[j][0] == "Enter" and lst[i][1] == lst[j][1]:
#                 ans.append("{0}님이 나갔습니다." .format(lst[j][2]))
# print(ans)
# 위에 코드 런타임 오류..

user = dict()
ans = []

for i in record:
    lst = i.split(' ')  # record의 요소를 띄어쓰기를 기준으로 나누어 배열안에 저장
    if lst[0] == 'Enter' or lst[0] == 'Change':  # 같은 아이디로 들어오거나 닉네임 수정을 하는 경우
        user[lst[1]] = lst[2]  # user에 저장
# 새롭게 갱신된 닉네임으로 결과 출력
for i in record:
    lst = i.split(' ')
    if lst[0] == 'Enter':
        ans.append('{0}님이 들어왔습니다.' .format(user[lst[1]]))
    elif lst[0] == 'Leave':
        ans.append('{0}님이 나갔습니다.' .format(user[lst[1]]))


print(ans)
