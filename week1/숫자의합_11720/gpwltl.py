leng = int(input())
nums = list(input())
ans = 0  # 변수 선언해야 함
for i in range(0, leng):  # leng대신 (1, leng+1)쓰면 런타임에러남!
    ans += int(nums[i])  # 리스트 값들 문자열-> 정수형
print(ans)
