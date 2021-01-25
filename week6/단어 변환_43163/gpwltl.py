from collections import deque as queue
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


# 파이썬 조건부 표현식 : (조건문이 참인 경우) if (조건문) else (조건문이 거짓인 경우)
# 내장함수 zip : 동일한 개수로 이루어진 자료형을 묶어주는 역할
def transistable(a, b): return sum((1 if x != y else 0)
                                   for x, y in zip(a, b)) == 1


def solution(begin, target, words):
    q = queue()  # deque([])
    d = dict()   # {}
    q.append((begin, 0))  # 0: level(answer)
    d[begin] = set(filter(lambda x: transistable(x, begin), words))

    # 해당 단어와 한글자만 빼고 동일한 단어 뽑아주기
    for w in words:
        d[w] = set(filter(lambda x: transistable(x, w), words))

    while q:
        cur, level = q.popleft()  # ('hit', 0)
        # words를 다 탐색해도 목표를 찾지 못한다면 0
        if level > len(words):
            return 0
        for w in d[cur]:
            if w == target:
                return level+1
            else:
                q.append((w, level+1))

    # q 모두 소비해서 못찾으면 0
    return 0


print(solution(begin, target, words))
