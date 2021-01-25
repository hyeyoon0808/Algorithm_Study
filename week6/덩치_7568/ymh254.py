n = int(input())

lst = []
rank = 1

for i in range(n):
    lst.append(list(map(int, input().split())))
for i in range(n):
    rank = 1
    for j in range(n):
        if i != j and lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank += 1
    print(rank, end=' ')
