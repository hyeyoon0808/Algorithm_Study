n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
# 끝나는 시간이 빠를 수록 회의의 수가 많아진다
# ab.sort(key=lambda x: x[0])
# 뒤에 요소만 소팅해주면 끝나는 시간이 같은 경우 시작시간을 고려하지않고 소팅하므로 앞에요소를 먼저 소팅해줘야함
# ab.sort(key=lambda x: x[1]) # lambda는 함수를 한줄로 만드는 형식으로 형태는 'lambda 인자 : 표현식'
# 밑 정렬에서는 x[1]이 정렬된 후에 x[1]이 같은 경우 x[0]을 sort해주는 듯!!
ab.sort(key=lambda x: (x[1], x[0]))

print(ab)
cnt = 0
last = 0
for i in range(n):
    if ab[i][0] >= last:
        last = ab[i][1]
        cnt += 1
print(cnt)
