def solution(numbers, target):
    sup = [0]
    for i in numbers:
        ch = []  # 다음 반복 때 계산을 해주기 위해 비움
        for j in sup:
            ch.append(j+i)
            ch.append(j-i)
        # sup에 append 된 ch값을 담는다
        sup = ch  # 마지막엔 모든 경우의 수를 담는다
    return sup.count(target)  # count 함수 : 주어진 값이 몇 개인지 센다.
