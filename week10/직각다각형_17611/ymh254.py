n = int(input())
xy = []
dic = dict()
for _ in range(n):
    xy.append(input())
# 처음 지점으로 돌아와야하므로 한 번더 추가
xy.append(xy[0])

dic_x = dict()
dic_y = dict()

px, py = map(int, xy[0].split())
for i in range(1, len(xy)):
    x, y = map(int, xy[i].split())
    # 시작좌표에서 다음 좌표까지의 구간 내에선 실선이므로 +1 다음 좌표(실선이 끝난 지점) 이후 -1
    # H와 교차점 갯수
    if x == px:
        start = min(y, py)
        end = max(y, py)
        if start in dic_y.keys():
            dic_y[start] += 1
        else:
            dic_y[start] = 1
        if end in dic_y.keys():
            dic_y[end] -= 1
        else:
            dic_y[end] = -1
    # V와 교차점 갯수
    if y == py:
        start = min(x, px)
        end = max(x, px)
        if start in dic_x.keys():
            dic_x[start] += 1
        else:
            dic_x[start] = 1
        if end in dic_x.keys():
            dic_x[end] -= 1
        else:
            dic_x[end] = -1
    px, py = x, y

# x, y 좌표선상 작은 수부터 큰 수까지 계산하기 위함
dic_x = sorted(dic_x.items(), key=(lambda x: x[0]))
dic_y = sorted(dic_y.items(), key=(lambda x: x[0]))
max_x = 0
temp_x = 0
for k, v in dic_x:
    temp_x += v
    max_x = max(max_x, temp_x)

max_y = 0
temp_y = 0
for k, v in dic_y:
    temp_y += v
    max_y = max(max_y, temp_y)

print(max(max_x, max_y))
