import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0] * n

if n >= 3:
    dp[0] = arr[0]  # 1칸일때
    dp[1] = max(arr[0]+arr[1], arr[1])    # 2칸일때
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])  # 3칸일때

    for i in range(3, n):  # 4칸 부터는 룰 적용(최댓값)
        # dp[n]=max(전전칸에서 올라온 경우, 직전 칸에서 올라온 경우)
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
    print(dp[n-1])

elif n == 2:
    print(max(arr[0]+arr[1], arr[1]))
elif n == 1:
    print(arr[0])
