record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
lst = []
ans = []
for i in range(len(record)):
    lst.append(list(record[i].split(" ")))
# print(lst)

for i in range(len(record)):
    if lst[i][0] == "Enter":
        ans.append("{0}님이 들어왔습니다." .format(lst[i][2]))
    elif lst[i][0] == "Leave":
        ans.append("{0}님이 나갔습니다." .format(lst[i][2]))
    else:
