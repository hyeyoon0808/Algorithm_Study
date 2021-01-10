leng = int(input())
time = list(map(int, input().split()))
answer = 0

time.sort()  # 정렬을 먼저 진행 후,
for i in range(leng):
    if i == 0:
        time[i] = time[i]  # 첫 번째는 그대로 배출
    else:
        time[i] = time[i-1]+time[i]  # 2번째부터 규칙 생성

for i in time:
    answer += i

print(answer)
