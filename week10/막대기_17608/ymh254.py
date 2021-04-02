import sys
# 그냥 input()으로 입력받으니까 런타임 에러 났다
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

m = lst[n-1]
cnt = 1
for i in range(n-2, -1, -1):
    if m == lst[i]:
        print("m1 "+str(m))
        print("add1 "+str(lst[i]))
        continue
    else:
        m = max(lst[i], m)
        print("m2 "+str(m))
        print("add2 "+str(lst[i]))
        if m == lst[i]:
            cnt += 1
print(cnt)
