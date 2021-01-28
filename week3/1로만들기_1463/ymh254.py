n = int(input())

temp = 1  # 1에서 더해나가는 방식
cnt = 0

if n == 1:
    print(0)
else:
    while True:
        if temp*3 < n:
            temp = temp*3
        elif temp*2 < n:
            temp = temp*2
        temp += 1
        cnt += 1
        if temp == n:  # temp랑 n이 같아졌을때 멈춤
            break
    print(cnt)
