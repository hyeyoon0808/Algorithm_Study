n = int(input())
l = list(map(int, input().split()))

ans = 0

# if len(l) == 1:
#     print(l[0])
# for i in range(n):
#     if l[i] == max(l):
#         while len(l) > 1:
#             if i-1 < 0:
#                 ans += max(l)+l[i+1]
#                 del l[i+1]
#             else:
#                 ans += max(l)+l[i-1]
#                 del l[i-1]
#     break
# 위에꺼는 왜 안되냐..

# 제일 높은 카드를 기준으로 인접된 카드가 합쳐짐
# 모든 카드들에 제일 높은 카드를 각각 합한 뒤 모든 카드를 합한 값
# 제일 높은 카드를 제외한 카드들의 합 + 제일높은카드 x n-1

for i in range(n):
    ans += l[i]
# 위에서 모든 카드를 합쳤으므로 max(l) * (n-2)를 해줌
print(ans + max(l) * (n-2))
