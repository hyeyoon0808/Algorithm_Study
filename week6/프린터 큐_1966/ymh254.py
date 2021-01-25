t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    v = [0] * n  # m이 있는 위치 표시
    v[m] = 1
    cnt = 0
    while True:
        if p[0] == max(p):  # 우선순위가 제일 큰 문서가 앞에 있을 경우
            cnt += 1    # 프린트를 하므로 +1을 해줌
            if v[0] == 1:  # 프린트한 문서가 m일 경우 cnt출력
                print(cnt)
                break
            else:   # m이 아닐 경우 없앤다
                del p[0]
                del v[0]
        else:  # 제일 큰수가 아닐 경우 맨 뒤로 미룬다
            p.append(p[0])
            v.append(v[0])
            del p[0]
            del v[0]
