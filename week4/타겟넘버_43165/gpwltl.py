answer = 0


def dfs(i, v, numbers, target):
    global answer
    if i == len(numbers) and v == target:
        answer += 1
        return
    if i == len(numbers):
        return
    # 더하거나 빼거나를 둘 다 작업해야하기에 파라미터에서 더함(v+numbers[i])과 뺌(v-numbers[i])을 적용할 것
    dfs(i+1, v+numbers[i], numbers, target)
    dfs(i+1, v-numbers[i], numbers, target)


def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)  # 처음 숫자도 +,-를 가질 수 있으니 0으로 시작할 것
    return answer


# 다른 풀이1  (product 이용 : 알아서 원소의 모든 요소의 조합을 구하는 라이브러리)
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)
