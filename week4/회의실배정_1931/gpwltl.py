import sys
input = sys.stdin.readline

leng = int(input())
meeting = []  # 회의 리스트

for _ in range(leng):
    start, end = map(int, input().split())
    meeting.append((start, end))  # sorted 사용하기위해?, (s, e)형식으로 배열에 추가

# 가장 빨리 끝나는 회의를 먼저 배정하고, 똑같은 시간에 끝나는 회의면 먼저 시작하는 회의를 우선순위로 둘 것.
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))


count = 1
# 첫 번째 회의가 끝나는 시간
prev = meeting[0][1]
for sch in meeting[1:]:
    # 다음 회의의 시작시간이 이전 회의가 끝나는 시간보다 크거나 같다 = 회의 열 수 있음
    if prev <= sch[0]:  # sch[0]은 meeting의 앞자리만, sch[1]은 뒷자리만
        prev = sch[1]
        count += 1

print(count)
