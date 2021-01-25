board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


# def d(answer, key):
#     answer.pop(key)
#     answer.pop(key)
#     return answer


def solution(board, moves):
    arr = [[] for _ in range(len(board))]
    for i in range(len(arr)):
        for j in range(len(board)):
            if board[j][i] != 0:
                arr[i].append(board[j][i])

    answer = []
    for m in moves:
        if arr[m-1]:  # 리스트에 값이 있을때만
            p = arr[m-1].pop(0)
            answer.append(p)

    # count = 0
    # for j in range((len(answer))//2):
    #     for i in range(len(answer)-1):
    #         if answer[i] == answer[i+1]:
    #             key = i
    #             d(answer, key)
    #             count += 2
    #             break

    # return count

    # 2) stack 이용!!
    stack = []
    count = 0
    for i in answer:
        stack.append(i)
        print(stack)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            count += 2

    return count


solution(board, moves)
