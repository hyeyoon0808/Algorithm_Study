Case = int(input())
person_info = [list(map(int, input().split())) for _ in range(Case)]

rank_list = [1] * Case
for i in range(len(person_info)):
    for j in range(len(person_info)):
        # 나 자신과의 비교를 제외. 없어도 정답임
        if(person_info[i][0] != person_info[j][0] and person_info[i][1] != person_info[j][1]):
            if((person_info[i][0] > person_info[j][0]) and (person_info[i][1] > person_info[j][1])):
                rank_list[j] += 1
print(*rank_list)