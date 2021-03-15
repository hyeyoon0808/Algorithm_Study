def solution(i, j):
    if j == c-1:
        return True
    for d in case:
        if 0 <= i+d < r and lst[i+d][j+1] == '.' and not visit[i+d][j+1]:
            visit[i+d][j+1] = True
            if solution(i+d, j+1):
                return True
    return False


r, c = map(int, input().split())
lst = [list(input()) for _ in range(r)]
# input()을 받거나 출력값의 처음이나 마지막에 공백이 있을경우
# input().strip()과 같이 stript()을 써줄 시 공백 제거
visit = [[False]*c for _ in range(r)]
case = [-1, 0, 1]
ans = 0
for i in range(r):
    if lst[i][0] == '.':
        if solution(i, 0):
            ans += 1
print(ans)
