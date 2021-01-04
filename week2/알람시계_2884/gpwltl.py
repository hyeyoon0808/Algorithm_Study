ansH = 0
ansM = 0
h, m = map(int, input().split())  # input은 string으로 받으니까 int로 변환
# m이 45분보다 작은지 큰지를 비교
if(m < 45):
    ansM = 60+(m-45)
    # 작을 때는 h가 0인 경우엔 23으로 설정
    if(h == 0):
        ansH = 23
    else:
        ansH = h-1
if(m >= 45):
    ansM = m-45
    ansH = h
print(ansH, ansM)
