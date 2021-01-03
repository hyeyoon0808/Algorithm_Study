n = input()
z = n.zfill(2)  # 0을 채우는 zfill() : str, int
answer = z
count = 0

while True:
    ans = str(int(z[0])+int(z[1]))
    ansZ = ans.zfill(2)
    z = z[1]+ansZ[-1]
    count += 1
    if z == answer:
        break

print(count)


# 다른 풀이
# 사람들은 주로 아래 방식으로 문제를 푸는 것을 발견할 수 있었음 : 수를 10으로 나눠 몫과 나머지로 자리수를 나눠서 풀이
# 메모리는 동일, 시간은 68-64ms로 유사 (하지만, 내 방식보다 코드를 알아보기 쉬움)
tmp = inp = int(input())
count = 0
while True:
    ten = tmp//10
    one = tmp % 10
    res = ten + one
    count += 1
    tmp = int(str(tmp % 10)+str(res % 10))

    if (inp == tmp):
        break
print(count)
