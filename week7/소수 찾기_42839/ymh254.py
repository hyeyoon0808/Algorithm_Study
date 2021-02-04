numbers = '17'


def sol(numbers):
    def dfs(word):
        if len(word) == k:
            result.add(int(word))
            return

        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1  # 중복되는 숫자 조합을 없애기 위함
                dfs(word + numbers[i])
                visit[i] = 0
        print(result)

    result = set()
    # 문자열을 아래와 같이 list로 받을 경우 문자 하나하나가 list의 요소로 저장됨
    numbers = list(numbers)
    n = len(numbers)
    visit = [0] * n
    for k in range(1, n+1):
        dfs("")

    # 소수 찾기
    answer = 0
    for i in result:
        if i == 1 or i == 0:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            answer += 1
    print(answer)

    return answer


sol(numbers)
