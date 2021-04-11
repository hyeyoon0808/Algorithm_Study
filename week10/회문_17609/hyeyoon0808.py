# 유사회문 판단 함수
def pseudo(a, left, right):
    while left < right:
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# 회문 판단 함수
def palindrome(a, left, right):
    while left < right:
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            res1 = pseudo(a, left+1, right)
            res2 = pseudo(a, left, right-1)
            if res1 == True or res2 == True:
                return 1
            else:
                return 2
    return 0

T = int(input())
for i in range(T):
    a = list(input())
    res = palindrome(a, 0, len(a)-1)
    print(res)