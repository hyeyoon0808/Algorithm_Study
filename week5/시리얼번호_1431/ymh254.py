n = int(input())
lst = [input() for _ in range(n)]
check = []
cnt = 0


for i in range(n):
    for j in lst[i]:  # enumerate쓰세요! for i, v in enumerate(lst):
        if j.isdecimal():  # isdecimal(): 숫자가 있는지 확인
            cnt += int(j)
    check.append((lst[i], cnt))
    cnt = 0
# print(check)
# 길이 => 숫자의 합 => 숫자&알파벳 순으로 비교하여 낮은 것을 앞으로 보낸다
check.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for i in range(n):
    print(check[i][0])
