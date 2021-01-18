array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []

    for x in commands:
        i = commands[0]
        j = commands[1]
        k = commands[2]  # 한번에 받아도됨! i,j,k=commands

        arr = array[i-1: j]
        arr.sort()
        answer.append(arr[k-1])

    return answer


print(solution(array, commands))


# 방법1 (13-15줄 대신)
# answer.append(list(sorted(array[i-1:j]))[k-1])

# 방법2 (아예 두줄로 끝..)
# def solution(array, commands):
#   return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
