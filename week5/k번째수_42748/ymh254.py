arr = list(map(int, input().split()))
com = [list(map(int, input().split())) for _ in range(3)]


def solution(arr, com):
    lst = []
    ans = []
    for i in range(len(com)):
        lst.append(arr[com[i][0]-1: com[i][1]])
    # ans = []
    # for i in range(len(com)):
        lst[i] = sorted(lst[i])
        ans.append(lst[i][com[i][2]-1])
    print(ans)
