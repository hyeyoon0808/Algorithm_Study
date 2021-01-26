global answer
def dfs(begin, target, words, visit):
    answer = 0
    stacks = [begin]
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer
        # 방문 여부를 words의 갯수만큼 0으로 초기화
        for i in range(len(words)):
            # 각 단어가 이전 비교값과 스펠링이 1개만 다르다면 방문여부 변경 & stacks에 추가
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:
                if visit[i] != 0:
                    continue
                visit[i] = 1
                stacks.append(words[i])
        answer += 1
    return answer

def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for i in words]
    answer = dfs(begin, target, words, visit)
    return answer​