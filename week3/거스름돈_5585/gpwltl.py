# 그리디
import sys
coin = int(sys.stdin.readline())
changes = 1000-coin
count = 0  # 잔돈에 포함된 매수

# 방법1
# def coins(changes, yen):
#     global count
#     count += changes//yen
#     global change  # 나누고 남은 잔돈
#     change = changes % yen
#     return change

# coins(changes, 500)
# coins(change, 100)
# coins(change, 50)
# coins(change, 10)
# coins(change, 5)
# coins(change, 1)


# 방법2(그리디)
change_money = [500, 100, 50, 10, 5, 1]
change = 0  # 큰 돈부터 빼고 남은 잔돈

for i in range(6):
    if changes >= change_money[i]:
        count += changes//change_money[i]
        change = changes % change_money[i]
        changes = change

print(count)
