triangle = eval(input())


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            # 아래 줄 숫자에 윗 줄 숫자를 더해가며 계산
            # 삼각형에서 제일 바깥쪽에 있는 두 수는 옵션이 하나 밖에 없음
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    # 삼각형의 맨 마지막 줄(마지막 배열) 중 제일 큰 숫자 출력
    return max(triangle[-1])


print(solution(triangle))
