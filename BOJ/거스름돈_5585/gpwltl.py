import sys
coin = int(sys.stdin.readline())
changes = 1000-coin
count = 0  # 잔돈에 포함된 매수


def coins(changes, yen):
    global count
    count += changes//yen
    global change  # 나누고 남은 잔돈
    change = changes % yen
    return change


coins(changes, 500)
coins(change, 100)
coins(change, 50)
coins(change, 10)
coins(change, 5)
coins(change, 1)

print(count)
