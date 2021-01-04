import sys
change = 1000 - int(sys.stdin.readline()) #잔돈 먼저 구해놓기
coin = [500, 100, 50, 10, 5] #코인 종류 리스트업
count=0

for i in coin:
    count += change // i #해당 코인으로 나눈 몫 더하기
    change = change % i #해당 코인으로 나눈 나머지 저장
count += change #잔돈에 포함된 매수 출력
print(count)
    