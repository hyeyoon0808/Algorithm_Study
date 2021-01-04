n = int(input())
answer = []  # 나올 수 있는 정답 넣어줄 리스트
ans = 0

for i in range(n//5+1):
    for j in range(n//3+1):
        if (5*i)+(3*j) == n:    # 넣어준 값 = (5*i)+(3*j)이 맞는 값 확인
            ans = i+j
            answer.append(ans)


if not answer:  # 빈 배열일 때 -1반환(if not 리스트)
    print(-1)
else:
    print(min(answer))  # 리스트에서 가장 작은 값 반환


# 다른 풀이(유사풀이)
# ** 내가 푼 것은 나올 수 있는 값을 모두 리스트에 넣고 리스트에서 가장 작은 값 호출(시간 오래걸림: 340ms)
# -> 그럴 필요가 없음 -> 5의 배수가 가장 큰 것부터 시작한다면 가장 작은 정답을 찾아낼 수 있음(시간 단축: 72ms)
def sugar(N):
    for y in range((N//3)+1):
        for x in range((N//5)+1):
            if ((5*x + 3*y) == N):
                return x+y

    return -1


N = int(input())  # 배달해야할 설탕 킬로그램
print(sugar(N))


# 다른 풀이2
# 5의 배수를 기준으로 배수이면 나눈 몫을 정답으로,
#   아니면 5의 배수가 될때까지 봉지는 1씩 추가하고 설탕은 3을 뺀 후 5의 배수가 됐을 때 몫을 추가(시간 짧게 소요: 68ms)
sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar % 5 == 0:  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else:
    print(-1)
