n = int(input())
word = [input()for _ in range(n)]

lst = {}

for i in range(n):
    l = len(word[i])  # l값을 포문이 돌 때마다 (하나의 글자를 비교할 때마다) -1씩 해줘야하므로!!
    for j in word[i]:
        if j in lst:
            lst[j] += 10**(l-1)
        else:
            lst[j] = 10**(l-1)  # {j : 10**(l-1)} 형태로 저장!
        l -= 1

sort_lst = sorted(lst.items(), key=lambda x: x[1], reverse=True)

ans = 0
for i in range(len(sort_lst)):
    ans += (9-i) * sort_lst[i][1]
print(ans)
