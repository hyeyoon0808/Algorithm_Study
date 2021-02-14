def solution(numbers):
    
    # 1~4자리까지 자리수별로 모으기 / 모두 12자리로 통일 해준다.
    numbers = [str(i) for i in numbers] # 모두 str로 변환
    com_list = []    
    for i in numbers :
        if len(i) == 4 :
            com_list.append([i,i*3])
        if len(i) == 3 :
            com_list.append([i,i*4])
        if len(i) == 2 :
            com_list.append([i,i*6])
        if len(i) == 1 :
            com_list.append([i,i*12])
    
    com_list.sort(key=lambda x:x[1],reverse=True)
    
    f_list = []
    for i in com_list :
        f_list.append(i[0])
    
    return str(int(''.join(f_list)))


# 다른 예시
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

