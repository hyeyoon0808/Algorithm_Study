# 시간 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# nlist = []

# for i in range(n):
#     nlist.append(int (input()))

# nlist.sort()

# for i in range(n):
#     print(nlist[i])

import sys
n = int(sys.stdin.readline())
cnt_list = [0]*10001 #10000보다 작거나 같은 자연수 -> 제한 걸어주기

for _ in range(n):
    cnt_list[int(sys.stdin.readline())]+=1 #해당 자리에 0에서 1로

for i in range(10001):
    if cnt_list != 0: # 1이상의 수로 초기화 된 경우
        for _ in range(cnt_list[i]): #입력된 수만큼 그 수를 출력
            print(i)