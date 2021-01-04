import math
a, b, v = map(int, input().split())
day = math.ceil((v-a)/(a-b))+1
print(day)

# ceil는 소숫점 올림
# (a-b)*n+a = v => (v-a)/(a-b)
# +1은 마지막날 (내려가지 않는다)