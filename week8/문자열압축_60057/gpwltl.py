s="ababcdcdababcdcd"    #2ababcdcd

def solution(s):
    result=""
    length=[]

    if len(s)==1:
        return 1
    
    for i in range(1, len(s)//2+1):    # //: 몫 구하기
        cut=s[:i]   #자를 단위
        count=1     #반복되는 수 저장
    
        for j in range(i, len(s), i):
            if cut==s[j:j+i]:
                count+=1
            else: 
                if count==1:
                    count=""
                result+=str(count)+cut
                cut=s[j:j+i]
                count=1

        if count==1: 
            count=""
        result+=str(count)+cut
        length.append(len(result))
        result=""

    return min(length)


print(solution(s))