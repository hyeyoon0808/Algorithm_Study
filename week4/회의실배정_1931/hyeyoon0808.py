#끝나는 시간이 빠른 순으로 정렬

import sys

n = int(sys.stdin.readline())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
#먼저, 시작 시간을 기준으로 정렬
s = sorted(s, key=lambda a: a[0])
#끝나는 사간을 기준으로 정렬
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
for start, finish in s:
    if start >= last:
        cnt += 1
        last = finish
print(cnt)