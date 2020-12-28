# answers = [1, 1, 1, 1, 1]

def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    result = [0, 0, 0]

    for i in range(len(answers)):
        if one[i % len(one)] == answers[i]:
            result[0] += 1
        if two[i % len(two)] == answers[i]:
            result[1] += 1
        if three[i % len(three)] == answers[i]:
            result[2] += 1

    for i in range(len(result)):
        if max(result) == result[i]:
            answer.append(i+1)


return answer
# print(answer)
