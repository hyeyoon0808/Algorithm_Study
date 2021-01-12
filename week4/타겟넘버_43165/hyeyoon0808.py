def solution(numbers, target):
    ans_list=[0] #첫 수부터 빼는 경우의 수 대비
    for i in numbers:
        temp_list=[]
        for j in ans_list:
            temp_list.append(j+i)
            temp_list.append(j-i)
        ans_list=temp_list
    answer = ans_list.count(target)
    return answer