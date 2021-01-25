import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    q = []
    N,M = map(int,input().split())
    queue = list(map(int,input().split()))
    for i in queue:
        q.append(i)
    p = M
    cnt = 0
    while(True):
        # q의 첫번째 원소가 max이면 pop
        if(max(q) == q[0]):
            q.pop(0)
            cnt += 1
            if(p == 0):
                print(cnt)
                break
            else:
                p -= 1
                if(p<0):
                    p = len(q)-1
        # pop한 뒤 맨뒤로 보냄
        else:
            p -= 1
            if(p<0):
                p = len(q)-1
            q.append(q.pop(0))