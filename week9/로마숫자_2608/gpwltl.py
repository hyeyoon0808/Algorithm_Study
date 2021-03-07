nums={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
extra={'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}    #예외까지 설정

#문자->숫자로 표현 함수
def to_num(r):
    res=0
    n=len(r)
    idx=0

    while idx<n:
        if idx==n-1:
            res+=nums[r[idx]]
            break

        flag=True
        if r[idx]=='I':
            if r[idx+1]=='V' or r[idx+1]=='X':
                res+=extra[r[idx:idx+2]]
                flag=False
        
        elif r[idx]=='X':
            if r[idx+1]=='L' or r[idx+1]=='C':
                res+=extra[r[idx:idx+2]]
                flag=False

        elif r[idx]=='C':
            if r[idx+1]=='D' or r[idx+1]=='M':
                res+=extra[r[idx:idx+2]]
                flag=False

        if not flag: 
            idx+=2
        else:
            res+=nums[r[idx]]
            idx+=1

    return res


a,b=input(), input()    #한줄에 하나씩 입력받을 때
a=to_num(a)
b=to_num(b)
total=a+b
print(total)    #첫번째 답: 숫자로 표현

ans=''
total=str(total)
t=len(total)
n=len(total)
while n:
    num=int(total[t-n])
    if n==4:
        ans+='M'*num
    elif n==3: 
        if num==9:
            ans+='CM'
        elif num==4:
            ans+='CD'
        else: 
            if num >= 5:
                ans+='D'
            ans+='C'*(num%5)

    elif n==2: 
        if num==9:
            ans+='XC'
        elif num==4: 
            ans+='XL'
        else:
            if num>=5:
                ans+='L'
            ans+='X'*(num%5)

    elif n==1: 
        if num==9:
            ans+='IX'
        elif num==4: 
            ans+='IV'
        else:
            if num>=5:
                ans+='V'
            ans+='I'*(num%5)
    
    n-=1

print(ans)      #두번째 답: 문자로 표현
