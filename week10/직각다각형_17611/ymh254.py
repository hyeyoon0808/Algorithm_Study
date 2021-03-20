n = int(input())
xy = []
dic = dict()
for _ in range(n):
    xy.append(list(map(int, input().split())))

for i in range(n):
    if xy[i][0] in dic:
        dic[xy[i][0]].append(xy[i][1])
    else:
        dic[xy[i][0]] = [xy[i][1]]

print(len(dic))
