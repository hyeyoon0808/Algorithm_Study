s = "ababcdcdababcdcd"

for i in range(1, int(len(s)//2 + 1)):

    n = ""
    cnt = 1

    re = s[:i]

    for j in range(i, len(s)+i, i):
        if re == s[j:j+i]:
            cnt += 1
        else:
            if cnt != 1:
                n = n + str(cnt) + re
            else:
                n = n + re

            re = s[j:j+i]
            cnt = 1
