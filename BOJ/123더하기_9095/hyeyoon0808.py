import sys

t = int(sys.stdin.readline())
dp = [1, 2, 4]

for i in range(3, 10):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in range(t):
    i = int(input())
    print(dp[i-1])

# dp 개념 복습
# f(n) = f(n-1) + f(n-2) + f(n-3)
