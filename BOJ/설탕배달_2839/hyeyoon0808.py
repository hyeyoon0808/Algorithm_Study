import sys
n = int(sys.stdin.readline())
total = 0

while True:
    if n%5 ==0:
        total += n//5 #5로 나눠지면 5로 나눈 몫
        break
    elif n <= 0:
        total = -1
        break
    n -= 3 #3은 while문으로 갯수 세어줌
    total += 1 #3의 개수

print(total)