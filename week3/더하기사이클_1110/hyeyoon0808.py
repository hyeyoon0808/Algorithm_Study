#1: 런타임 에러 - 이유 모름 ㅜ
# import sys
# n = sys.stdin.readline()
# if len(n)==1:
#     n="0"+n
# new = n
# count=0
# while n!=new or count ==0:
#     n=n[-1]+str(int(n[0])+int(n[1]))[-1] #-1을 사용하여 n의 마지막 문자열과 합한 문자열의 마지막 더하기
#     count +=1

# print(count)

#2
A = int(input())
N = A%10*10 +(A//10+ A%10)%10 #일의 자리수에 10을 곱한 것 + 두번째 자리수와 일의 자리수의 합에 10으로 나눈 몫
count =1
while A!=N: #두수가 같아질때까지
    N= N%10*10 +(N//10+ N%10)%10
    count += 1
print(count)


