from collections import deque
import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    priority = deque(map(int, input().split()))
    count = 0

    while priority:
        top = max(priority)
        m -= 1
        v = priority.popleft()

        if top != v:  # 빠진수가 우선순위가 아니라면 다시 리스트에 넣어주기
            priority.append(v)
            if m < 0:  # 찾을 수의 위치기억(빠져나갈때 위치가 -1)
                m = len(priority)-1
        else:
            count += 1
            if m == -1:
                print(count)
                break
