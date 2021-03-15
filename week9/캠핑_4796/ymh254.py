lst = []
while True:
    lpv = list(map(int, input().split()))
    lst.append(lpv)
    if lpv == [0, 0, 0]:
        break

for i in range(len(lst)-1):
    ans = 0
    # 남은 일 수가 l보다 클 경우 (min으로) 예외처리
    ans = lst[i][2]//lst[i][1]*lst[i][0]+min(lst[i][2] % lst[i][1], lst[i][0])
    print(f"Case {i+1}: {ans}")
