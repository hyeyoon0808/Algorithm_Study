s = "aabbaccc"


def solution(s):
    if len(s) == 1:
        return 1

    lst = []
    for i in range(1, len(s)//2 + 1):
        x = s[:i]
        cnt = 1
        re = ""
        for j in range(i, len(s)+i, i):
            if x == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    re = re + str(cnt) + x
                else:
                    re = re + x
                x = s[j:j+i]
                cnt = 1
        lst.append(len(re))

    return min(lst)


print(solution(s))
