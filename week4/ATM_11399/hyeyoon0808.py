n=int(input())
time=list(map(int,input().split()))
#오름차순으로 정렬
time.sort()
sumTime=0
prev=0
#각 시간을 이전꺼에 더한것들을 합산하기
for i in time:
  prev+=i
  sumTime+=prev

print(sumTime)