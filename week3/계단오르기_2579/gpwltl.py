# DP
import sys
input = sys.stdin.readline
leng = int(input())
arr = []    # 계단의 각 점수
dp = [0]*leng   # 저장할 dp 리스트

for _ in range(leng):
    arr.append(int(input()))

# if~elif문 안쓰면 런타임 에러 : dp[0],dp[1],dp[2]로 초기화했지만 arr의 개수가 이보다 적어서 런타임에러 발생시킴
if leng >= 3:
    dp[0] = arr[0]  # 1칸일때
    dp[1] = max(arr[0]+arr[1], arr[1])    # 2칸일때
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])  # 3칸일때

    for i in range(3, leng):  # 4칸 부터는 룰 적용(최댓값)
        # dp[n]=max(전전칸에서 올라온 경우, 직전 칸에서 올라온 경우)
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
    print(dp[leng-1])

elif leng == 2:
    print(max(arr[0]+arr[1], arr[1]))
elif leng == 1:
    print(arr[0])


# 알아볼 것
# if __name__ == '__main__'
