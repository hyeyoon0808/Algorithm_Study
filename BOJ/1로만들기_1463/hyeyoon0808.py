# dp를 사용하지 않음
# import sys
# n = int(sys.stdin.readline())
# temp = 1 #1에서 더해나가는 방식
# count = 0

# if n ==1:
#     print(0)
# else:
#     while True: 
        
#         if temp*3 < n:
#             temp = temp*3
#         elif temp*2 <n:
#             temp = temp*2
#         temp += 1
#         count += 1
#         if temp == n: #temp랑 n이 같아졌을때 멈춤
#             break

#     print(count)

#다른사람 코드
testcase=int(input())
 
dp=[ 0 for _ in range(testcase+2) ]
dp[2]=1
 
for i in range(2, len(dp)):
 
    dp[i]=dp[i-1]+1
 
    if i%3==0:
        if dp[i]> dp[int(i/3)]+1:
            dp[i]=dp[int(i/3)]+1
    if i%2==0:
        if dp[i]> dp[int(i/2)]+1:
            dp[i] =dp[int(i/2)]+1
 
print(dp[testcase])
