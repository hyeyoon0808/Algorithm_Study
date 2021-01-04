n = 5
lost = [2, 4]
reserve = [3]
students = [1]*n    # n명의 리스트 만들기(초기화 : 1)
answer = 0  # 체육복 있는 학생 수

for i in reserve:
    students[i-1] = 2   # 여분있는 학생들은 2개로 지정
for i in lost:
    # 0으로 두면 안됨(조건: '여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다')
    students[i-1] = students[i-1]-1

for i, v in enumerate(students):
    # '양쪽 친구 중' 2인 친구에게 빌림(0번째와 마지막 친구 제외) -> i조건을 둔 이유
    if i < n-1 and v == 0 and students[i+1] == 2:   # 마지막은 앞에서만 빌리기에 elif문 따름
        students[i] = students[i+1] = 1
    elif i > 0 and v == 0 and students[i-1] == 2:   # 0번째는 뒤에서만 빌리기에 if문을 따름
        students[i] = students[i-1] = 1

for i in students:
    if i == 1 or i == 2:    # 체육복 가지고 있는 친구들 카운트
        answer += 1

print(answer)
