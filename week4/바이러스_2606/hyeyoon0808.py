#경로의 특징이 있기 때문에 dfs가 유리하다 판단하여 DFS 사용
# import sys 

# link = [] 

# computer = int(sys.stdin.readline())
# net_computer = int(sys.stdin.readline())

# #빈차열 미리 채워두기
# for _ in range(computer+1): 
#     link.append([0] * (computer+1)) 

# # 각각 인접한 노드들 리스트로 정리
# for _ in range(net_computer): 
#     list = list(map(int, input().split()))
#     # 앞뒤 바꾼 행렬 생성: matrix[행 열]
#     matrix[link[0]][link[1]] = 1
#     matrix[link[1]][link[0]] = 1

# def bfs(start):
#     queue=[start]
#     check = [start]
#     while queue:
#         current = queue.pop(0)
#         for i in range(len(matrix[current])):
#             if matrix[current][i] and i not in check:
#                 check += [i]
#                 queue += [i]
#     return len(check) -1

# print(dfs(1))

import sys
r = sys.stdin.readline


def dfs(v, egs, ans):
    for i in egs[v]:
        if i not in ans:
            ans.append(i)
            dfs(i, egs, ans)
    return ans


N = int(r())
#빈차열 미리 채워두기
edges = [[] for _ in range(N+1)]
# 각각 인접한 노드들 리스트로 정리
for _ in range(1, int(r())+1):
    e1, e2 = map(int, r().split())
    edges[e1].append(e2)
    edges[e2].append(e1)

print(len(dfs(1, edges, [1]))-1)

