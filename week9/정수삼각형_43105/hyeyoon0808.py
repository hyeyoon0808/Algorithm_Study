def solution(triangle):
    answer =0
    
    for i in range(1, len(triangle)): #이후 연산에 i-1시점의 값을 더하기 때문에 0부터 시작이 아니라 1부터 시작
        for j in range(i+1): # 모든 원소를 순회해야 하기 때문에 i+1개
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == i:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max([triangle[i-1][j], triangle[i-1][j-1]])
    return max(triangle[len(triangle)-1])