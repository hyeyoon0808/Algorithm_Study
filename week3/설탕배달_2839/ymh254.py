# sugar bag
n = int(input())
# the number of cases
# nums = []

# if n % 5 == 0:  # n이 5로 나눠질 때
#     print(n / 5)
# elif n % 5 != 0:  # n이 5로 안 나눠질 때
# 위는 생략가능
# temp = 0

# if n // 5 == 0 and n % 3 == 0:  # n을 5로 나눈 몫이 0이면서 n이 3으로 나눠질 때
#     print(n/3)
# elif n // 5 > 0:  # n을 5로 나눈 몫이 0보다 클 때
#     for i in range(n//3+1):  # 0부터 n을 3으로 나눈 몫까지
#         for j in range(n//5+1):  # 0부터 n을 5로 나눈 몫까지
#             if 3*i + 5*j == n:  # 5를 최대한으로 사용하기 위해 j를 곱해줌
#                 temp = 3*i + 5*j
#                 print(i+j)
#                 break
#         if temp == n:
#             break   # break를 사용하면 처음 값에서 멈출 수 있음.
#     #             nums.append(i+j)
#     # print(nums[0]) # 리스트에 넣어 주고 처음 값만 출력할 시 런타임 에러
# else:
#     print(-1)


def sugar(n):
    for i in range((n//3)+1):
        for j in range((n//5)+1):
            if ((3*i + 5*j) == n):
                return x+y

    return -1


print(sugar(n))

# 함수에서 리턴을 할 시 for문이 돌면서 출력되는 여러 값 중 제일 가까운 값만 리턴됨
