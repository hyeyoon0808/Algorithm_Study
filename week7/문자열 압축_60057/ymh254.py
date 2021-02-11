s = "xababcdcdababcdcd"


def solution(s):
    leng = []

    if len(s) == 1:
        return 1

    # n개 단위로 비교 시 n은 s를 반으로 나눈 값보다 클 수 없음
    for i in range(1, int(len(s)//2 + 1)):
        n = ""
        cnt = 1
        rep = s[:i]
        # rep 이후부터 비교하면 되므로 i를 1부터 받아옴
        # rep의 길이만큼 비교를 해주기위해 세번째 인자로 i를 설정
        for j in range(i, len(s)+i, i):
            if rep == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    n = n + rep
                else:
                    n = n + str(cnt) + rep

                rep = s[j:j+i]
                cnt = 1
        leng.append(len(n))
    return min(leng)


print(solution(s))
