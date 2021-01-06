num = int(input())
alist=list()
blist=list()
for i in range(num):
    a, b = map(int, input().split()) #각 숫자 input
    #a, b list에 저장
    alist.append(a)
    blist.append(b)

for x in range(num):
    #list 더해주기
    print(alist[x]+blist[x])