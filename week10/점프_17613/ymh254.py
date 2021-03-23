t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    max = 0
    for j in range(x, y+1):
        a = 1  # 뛰는 범위
        sum = 1  # 두배씩 증가하여 뛰는 a의 합
        cnt = 1  # 뛴 횟 수
        while j != 0:
            while True:
                a *= 2
                sum += a
                # sum이 도착해야할지점보다 클 경우
                # 직전으로 복귀 시킨 후 while문을 나옴
                if sum > j:
                    sum -= a
                    a = a/2
                    break
                cnt += 1
            # 남은 범위 계산
            # 뛰는 범위와 합을 1로 되돌림
            j -= sum
            if j > 0:
                sum = 1
                a = 1
                cnt += 1
        if max < cnt:
            max = cnt
    print(max)
