import sys

input=sys.stdin.readline

n=input()
c=list(map(int, input().split()))

c.sort(reverse=True)
result = c[0]*(int(n)-2) + sum(c)
print(result)