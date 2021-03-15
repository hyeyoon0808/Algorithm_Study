n = int(input())
number = int(input())


def solution(n, number):
    if n == number:
        return 1
    # 최솟값을 8까지만 구하면 됨
    # 중복을 없애기 위해 빈 set을 생성
    s = [set() for _ in range(8)]
    for i in range(8):
        s[i].add(int(str(n)*(i+1)))
    for i in range(1, 8):
        for j in range(i):
            # ex)
            # n이 3일 경우
            # s[0](n이 1일 경우의 수)과 s[1](n이 2일 경우의 수)
            # s[1](n이 2일 경우의 수)과 s[0](n이 1일 경우의 수)을 사칙연산 한 경우를 모두 구해주면 됨
            for a in s[j]:
                for b in s[i-j-1]:
                    s[i].add(a+b)
                    s[i].add(a-b)
                    s[i].add(a*b)
                    if b > 0:
                        s[i].add(a//b)
        if number in s[i]:
            return i+1
    return -1
