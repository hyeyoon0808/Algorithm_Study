def solution(N, number):
    possible_set = [0,[N]] # 조합으로 나올수 있는 가능한 숫자들
    if N == number: #주어진 숫자와 사용해야 하는 숫자가 같은 경우 1개
        return 1
    for i in range(2, 9): 
        case_set = [] 
        basic_num = int(str(N)*i) 
        case_set.append(basic_num)
        for i_half in range(1, i//2+1): # 절반 이상으로 넘어가면 같은 결과 반복 
            for x in possible_set[i_half]:
                for y in possible_set[i-i_half]: # x와 y를 더하면 i 가 되도록
                    print(possible_set)
                    case_set.append(x+y)# 각 사칙연산 결과를 더함
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y !=0:
                        case_set.append(x/y)
                    if x !=0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set) # 최종 결과물 set에 사칙 연산 결과를 더함
    return -1 #N 이 8까지 답이 없으면 -1을 출력