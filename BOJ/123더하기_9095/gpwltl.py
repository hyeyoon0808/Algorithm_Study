leng = int(input())
ans = []
# 1은 1가지(1+1+1+1), 2는 2가지(1+1, 2), 3은 4가지(1+1+1, 1+2, 2+1, 3)
dic = {1: 1, 2: 2, 3: 4}

for n in range(4, 11):  # 'n은 양수이며 11보다 작다' - 10까지의 값을 정한다.
    # n=5, 1+(4의 총케이스) + 2+(3의 총케이스) + 3+(2의 총케이스) -> (n-1)총케이스+(n-2)총케이스+(n-3)총케이스
    dic[n] = dic[n-1]+dic[n-2]+dic[n-3]
for i in range(leng):
    num = int(input())
    ans.append(dic[num])

for i in ans:
    print(i)
