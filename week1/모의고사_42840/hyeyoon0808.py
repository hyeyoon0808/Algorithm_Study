# temp1 : 10.2 ~ 10.3m
answers = list(map(int, input().split()))
answer = []
# a, b, c 로 나누어 패턴 정렬
a = [1,2,3,4,5]
b = [2,1,2,3,2,4,2,5]
c = [3,3,1,1,2,2,4,4,5,5]
countA = 0
countB = 0
countC = 0

lenAns = len(answers)

# 각각 정답과 비교해서 같은 경우 정답수 저장
for i in range(lenAns):
    if answers[i] == a[i%len(a)]: # 리스트 길이 나머지 값으로 정렬 비교
            countA += 1
    if answers[i] == b[i%len(b)]:
        countB += 1
    if answers[i] == c[i%len(c)]:
        countC += 1
        
# a, b, c 순서대로 정답 수 나열
countABC = [countA, countB, countC]

# countABC 리스트 최댓값과 같은 사람 리스트에 저장
# list 는 배열을 인덱스로 접근해야 함. 
# enumerate 는 지연 제너레이터(lazy generator)로 이터레이터 감싸서 이터레이터에서 루프 인덱스와 다음 값을 한 쌍으로 가져와 넘김.
for person, count in enumerate(countABC):    
    print(count)                             
    if count == max(countABC):
        answer.append(person +1)

# # 정답자 출력
# for i, p in enumerate(answer):
#     print(p)
        





# temp2 : 다른 사람 풀이
answers = list(map(int, input().split()))
# 2차원 리스트 활용
p = [[1,2,3,4,5],
    [2,1,2,3,2,4,2,5],
    [3,3,1,1,2,2,4,4,5,5]] # index=i : 0~3, 값=v: 3개의 list
# p의 길이만큼 늘리기
s = [0] * len(p)
# s i=0 => 첫번째 리스트
# s i=1 => 2번째 리스트
# s i=2 => 3번째 리스트

# answers = 1345 index = q: 0~3, 값 = a: 1,3,4,5

# 이중 for loop
for q, a in enumerate(answers): # q =0 a=1
    for i, v in enumerate(p): # v는 각각 리스트의 길이인 5,6,7
        if a == v[q % len(v)]: # 나머지 값과 비교
            s[i] += 1 
return [i+1 for i, v in enumerate(s) if v == max(s)]





# temp3 : 다른 사람 풀이
# itertools : 반복 가능한 데이터 원소들을 처리 함수&레이터
# cycle : 
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]