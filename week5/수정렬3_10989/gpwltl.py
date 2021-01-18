import sys
input = sys.stdin.readline

n = int(input())
array = [0]*10001

for _ in range(n):
    array[int(input())] += 1

for i in range(len(array)):
    if array[i] > 0:
        for j in range(array[i]):
            print(i)


# 메모리 제한 문제로 모든 수를 리스트에 저장하고 정렬하면 안됨 -> 카운팅(계수 정렬) 필요
# 계수 정렬 : 값을 저장하지 않고 동일한 인덱스에 카운트해준 뒤 그 정보만 프린트
