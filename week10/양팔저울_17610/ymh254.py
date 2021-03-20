def dfs(x, total):
    if total > s:
        return
    if x == k:
        if 0 < total <= s:
            ch[total] = 1
    else:
        # k의 개로 만들 수 있는 모든 경우의 수 생성
        dfs(x+1, total+lst[x])
        dfs(x+1, total-lst[x])
        dfs(x+1, total)


k = int(input())
lst = list(map(int, input().split()))
s = sum(lst)
ch = [0] * (s+1)
dfs(0, 0)
cnt = 0
for i in ch:
    if i == 0:
        cnt += 1
# ch에서 s+1만큼 check했으므로 [0]번째 0 제외 후 출력
print(cnt - 1)


# set 이용 코드
# def DFS(L,total):
#     global s
#     global res
#     if total>s:
#         return
#     if L==k:
#         if 0<total<=s:
#             res.add(total)
#     else:
#         DFS(L+1,total+w[L])
#         DFS(L+1,total-w[L])
#         DFS(L+1,total)

# k=int(input())
# w=list(map(int,input().split()))
# s=sum(w)
# res=set()
# DFS(0,0)
# print(s-len(res))
