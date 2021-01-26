b = "hit"
t = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def sol(b, t, words):
    if t not in words:
        return 0
    else:
        ans = 0
        lst = [b]
        while t not in lst:
            for i in lst:
                lst2 = []
                for w in words:
                    cnt = 0
                    for j in range(len(b)):
                        if i[j] != w[j]:  # 글자 하나하나 비교하여 다른 글자 수만큼 cnt +1
                            cnt += 1
                        if cnt == 2:  # cnt가 2가 되면 단어를 대체할 수 없으므로 바로 break
                            break
                    if cnt == 1:
                        # lst.append(w) # 기존 배열에 추가하면 전에 있던 요소가 중복되므로
                        lst2.append(w)  # 새로 들어오는 원소를 새 배열에 받은 뒤 대체해줌
                        words.remove(w)
            # lst2가 아예 다른 값으로 갱신 될 때마다 + 1 (조건이 충족한다면 두 개의 요소가 lst2에 추가 될 수 있음)
            ans += 1
            if t in lst2:
                return ans
            else:
                lst = lst2
        return 0


print(sol(b, t, words))
