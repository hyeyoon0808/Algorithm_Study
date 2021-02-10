s="ababcdcd"

def solution(s):
    length=[]
    result=""

    if len(s)==1:
        return 1

    for cut in range(1, len(s)//2+1): 
        count=1
        tempStr = s[:cut]   #자를 단위(a, ab, aba, abab)

        for i in range(cut, len(s), cut):
            if s[i:i+cut]==tempStr:
                count+=1
            else: 
                if count==1:    #카운트가 1이면 생략하고 붙이기 위해 빈칸으로 설정
                    count=""
                result += str(count)+tempStr
                tempStr=s[i:i+cut]
                count=1
        
        if count==1:
            count=""
        result += str(count)+tempStr
        length.append(len(result))
        result=""

    return min(length)      #가장 짧은 길이 반환


print(solution(s))