n = int(input())
p = list(map(int, input().split()))

lst = [0] * (n+1)  # 리스트 뒤로 가면서 누적되는 값을 담기위한 배열

p.sort()  # 제일 큰 수가 마지막에 올 경우 누적 값의 합이 작아진다
# 처음 사람이 걸리는 시간은 0이므로 배열 앞에 0을 추가해준다


def time():
    for i in range(1, n+1):
        lst[i] = lst[i-1]+p[i-1]
    print(sum(lst))


time()
