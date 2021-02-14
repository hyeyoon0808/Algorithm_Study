import math
import itertools

# 소수인지 판별해주는 함수
def is_decimal(n):
    if n < 2: return False

    to = int(math.sqrt(n)) + 1
    for i in range(2, to):
        if n % i == 0: return False
    return True

def solution(number):
    candidate = set()

    for i in range(len(number)):
        numbers = set(map(int, map(''.join, itertools.permutations(number, i+1))))
        candidate |= numbers # 합집합

    answer = 0
    candidate = list(candidate) # 리스트 변환
    for n in candidate:
        if is_decimal(n):
            answer += 1
    return answer