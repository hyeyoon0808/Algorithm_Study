import math

n = input()
x = math.floor(len(n)/10)
for i in range(x):
    print(n[0+10*i: 10+10*i])
print(n[0+10*x: 10+10*(x-1)+(len(n) % 10)])
