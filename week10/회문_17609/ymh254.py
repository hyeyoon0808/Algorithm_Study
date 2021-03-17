import sys
input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     w = input()
#     rw = w[::-1]
#     if w == rw:
#         print(0)
#     else:
#         for i in range(len(w)):
#             if w[i] == rw[i]:
#                 continue
#             else:
#                 w = w.replace(w[i], "")
#                 rw = rw.replace(rw[-1-i], "")
#                 break
#         if w == rw:
#             print(1)
#         else:
#             print(2)
# 위에꺼 반례가 뭐 있지..ㅜㅜ


def sol(w):
    left = True
    right = True
    for i in range(len(w)//2):
        # 왼쪽 끝과 오른쪽 끝을 비교하여 틀릴 시,
        if w[i] != w[-1-i]:
            for j in range(i, len(w)//2):
                # 왼쪽 끝에서 비교 된 문자 다음 문자와 원래 오른쪽 끝에서 비교 된 문자부터 비교
                # 즉, 틀린 글자 중 왼쪽 글자 배제 후 비교
                if w[j+1] != w[-1-j]:
                    left = False
                # 오른쪽 끝에서 비교 된 문자 전 문자와 원래 왼쪽 끝에서 비교 된 문자부터 비교
                # 즉, 틀린 글자 중 오른쪽 글자 배제 후 비교
                if w[j] != w[-1-j-1]:
                    right = False
            if not left and not right:
                return 2
            elif not left or not right:
                return 1
    return 0


t = int(input())
for _ in range(t):
    print(sol(input().rstrip()))
# rstrip()안쓰면 틀림..
