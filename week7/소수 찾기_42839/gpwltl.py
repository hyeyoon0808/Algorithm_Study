import math 
from itertools import permutations 

def is_decimal(n):
    if n<2: return False

    to = int(math.sqrt(n))+1    # math.sqrt() : 제곱근
    for i in range(2, to):
        if n%i==0: return False

    return True


def solution(numbers):
    candidate = set()

    for i in range(len(numbers)):
        number=set(map(int, map(''.join, permutations(numbers, i+1))))
        candidate  |= number   #합집합

    answer=0
    candidate=list(candidate)   #리스트 변환
    for n in candidate:
        if is_decimal(n):   #소수 판별 함수로 소수인지 파악 
            answer += 1
    return answer


# 소수 찾는 방법 : '에라토스테네스의 체'
# -> 범위에서 합성수를 지우는 방식으로 소수 찾는 방식