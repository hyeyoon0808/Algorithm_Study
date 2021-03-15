r1 = input()
r2 = input()


def solution(r):
    ans = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(r)):
        if i > 0 and rom[r[i]] > rom[r[i-1]]:
            ans += rom[r[i]] - rom[r[i-1]]*2    # 전에 더해진 인덱스값을 두번 빼야함
        else:
            ans += rom[r[i]]
    return ans


def solution2(n):
    ans = ""
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC",
           "L", "XL", "X", "IX", "V", "IV", "I"]
    for i in range(len(num)):
        start = n // num[i]
        ans += rom[i] * start
        n -= num[i] * start
    return ans


print(solution(r1) + solution(r2))
print(solution2(solution(r1) + solution(r2)))
