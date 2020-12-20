def solution(answers):
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    cnt = [0, 0, 0]

    # 정답과 각 수포자의 답을 비교한 뒤, 맞을 때 카운트 증가
    for i in range(len(answers)):
        if(answers[i] == person1[i % 5]):
            count[0] += 1
        if(answers[i] == person2[i % 8]):
            count[1] += 1
        if(answers[i] == person3[i % 10]):
            count[2] += 1

    # count에서 가장 큰 수 찾고,
    maxNum = max(count)
    # 가장 큰 수와 동일한 값 갖고 있는 번호를 answer에 추가해주기
    if(count[0] == maxNum):
        answer.append(1)
    if(count[1] == maxNum):
        answer.append(2)
    if(count[2] == maxNum):
        answer.append(3)

    return answer
