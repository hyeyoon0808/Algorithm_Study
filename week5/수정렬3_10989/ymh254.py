import sys

input = sys.stdin.readline

n = int(input())

lst = [0] * 10001  # 숫자 크기 범위
# 들어오는 숫자를 lst의 인덱스로 받아 해당하는 자리에 +1씩해준다
for _ in range(n):
    a = int(input())
    lst[a] += 1
    # lst[int(input())] += 1로 합치기 가능

for i in range(len(lst)):
    if lst[i] == 1:  # lst의 인덱스가 1일경우 인덱스값을 한번 출력
        print(i)
    elif lst[i] > 1:  # 1이 아닌 경우 그 만큼 출력 해줌
        for _ in range(lst[i]):
            print(i)

# 밑의 코드는 메모리 초과..
# n = int(input())

# lst = []
# for _ in range(n):
#     lst.append(int(input()))

# v = 0
# for i in range(n-1):
#     v = lst.pop()
