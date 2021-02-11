n = int(input())
a, b = map(int, input().split())
m = int(input())
xy = []
for _ in range(m):
    xy.append(list(map(int, input().split())))

dic = dict()
for x, y in xy:
    if x in dic:
        y = str(y)
        dic[x].append(y)
        y = int(y)
    else:
        dic[x] = y

print(dic)
