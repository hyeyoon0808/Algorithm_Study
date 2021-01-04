import math

A, B, V = list(map(int, input().split()))
# dis = 0
# day = 0
# while True:
#     day += 1
#     dis += (A - B)
#     if dis+A >= V:
#         print(day+1)
#         break
#     elif dis+A < V:
#         if dis == V:
#             print(day)
#             break

# 넘나 어렵게 생각했다...

day = math.ceil((V-A)/(A-B))+1
print(day)
print((V-A)/(A-B))
