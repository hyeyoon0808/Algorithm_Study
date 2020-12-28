import math
a, b, v = map(int, input().split())
date = (v-a)/(a-b)+1
answer = math.ceil(date)

print(answer)

# 반복문으로 풀면 '시간초과'
# 하루 올라갈 미터(a-b), 걸리는 일수(date) : (a-b)*date + a = v
# +1은 다 올라가면 내려오지 않아서 올라간 마지막날을 더해준 것
# 일수가 소수점이면 올림(math.ceil(i))할 것
