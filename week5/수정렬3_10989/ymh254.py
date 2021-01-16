n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))
v = []
v = lst.pop()
print(lst)
print(v)

# v = 0
# for i in range(n-1):
#     v = lst.pop()
