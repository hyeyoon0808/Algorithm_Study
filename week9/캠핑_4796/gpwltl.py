import sys
input=sys.stdin.readline

answer=[]
a=1
while True: 
    l, p, v=map(int, input().split())
    day=0

    if l+p+v==0:      #0 0 0일때 끝나기 
        break
    else:
        # k=0     #가장 마지막의 p의 배수
        # for i in range(1,v+1):    #for문은 시간초과
        #     if i%p==0:
        #         day+=(1*l)
        #         k=i
        # day+=v-k

        day=(v//p)*l
        day+=min((v%p), l)

        print('Case %d: %d' %(a, day))
        a+=1
