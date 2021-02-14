def solution(s):
    LENGTH = len(s)
    cand = [LENGTH]  # 1~len까지 압축했을때 길이 값

    for size in range(1, LENGTH):
        compressed = ""
        # string 갯수 단위로 쪼개기 *
        splited = [s[i:i+size] for i in range(0, LENGTH, size)]
        count = 1

        for j in range(1, len(splited)):
            prev, cur = splited[j-1], splited[j]
            if prev == cur:  # 이전 문자와 동일하다면
                count += 1
            else:  # 이전 문자와 다르다면
                compressed += (str(count) + prev) if count > 1 else prev
                count = 1  # 초기화

        compressed += (str(count) + splited[-1]) if count > 1 else splited[-1]
        cand.append(len(compressed))

    return min(cand)  # 최솟값 리턴