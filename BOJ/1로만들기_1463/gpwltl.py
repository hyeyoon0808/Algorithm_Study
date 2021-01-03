# DP
import sys
x = int(sys.stdin.readline())
dp = [0 for _ in range(x+1)]  # dp=[0,0,0,0,0,,,,] : x 크기의 배열 생성

for i in range(2, x+1):  # dp[2]부터 저장
    dp[i] = dp[i-1]+1  # 1을 뺀 값, 2의 배수, 3의 배수 중 최솟값을 찾는다.
    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2]+1
    if i % 3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3]+1

print(dp[x])


# 다른 풀이dp - min
# dp[n] = min(dp[n/3], dp[n/2], dp[n-1])+1
x = int(input())
dp = [0 for _ in range(x+1)]


def temp(n):
    for i in range(2, n+1):
        dp[i] = dp[i-1]+1   # 앞에꺼보다 +1, 2의 배수이거나 3의 배수면
        if i % 3 == 0:
            # 앞에꺼에 +1한 것 'dp[i]' 과 'dp[i//3]+1'한 것과 비교
            dp[i] = min(dp[i], dp[i//3]+1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
    return dp[n]


print(temp(x))
