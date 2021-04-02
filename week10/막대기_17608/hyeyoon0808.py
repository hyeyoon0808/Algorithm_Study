import sys
input = sys.stdin.readline

n = int(input())
nList = []

for _ in range(n):
    nList.append(int(input()))
#가장 마지막 수를 가장 큰 숫자로
nListMax=nList[n-1]
count=1
# 뒷 숫자부터 순차적으로 가장 큰수랑 비교
for i in range(n):
    if nListMax < nList[n-2-i]: 
        count+=1
        nListMax = nList[n-2-i]
print(count)