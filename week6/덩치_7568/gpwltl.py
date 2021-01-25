import sys
input = sys.stdin.readline

n = int(input())
_arr = []
rank = 1
for _ in range(n):
    weight, height = map(int, input().split())
    _arr.append([weight, height, rank])  # 리스트로 넣어줌(튜플이면 값을 변경할 수가 없어서)

# rank는 자기보다 큰 것을 발견할때마다 개수를 1씩 증가시켜 자신의 순위를 찾음
for i in _arr:
    for j in _arr:
        if i == j:
            continue
        if i[0] < j[0] and i[1] < j[1]:
            i[2] += 1
    print(i[2], end=" ")
