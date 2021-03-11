def solution(N, number):
    S=[0, {N}]
    for i in range(2,9):
        case_set={int(str(N)*i)}
        for j in range(1, i//2+1):
            for x in S[j]:
                for y in S[i-j]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(x*y)
                    
                    if x!=0:
                        case_set.add(y//x)
                    
                    if y!=0:
                        case_set.add(x//y)
        
        if number in case_set:
            return i
        S.append(case_set)

    return -1

print(solution(2,11))