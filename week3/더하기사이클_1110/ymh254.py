n = int(input())  # n을 숫자로 받아야 10보다 큰지 비교 가능
m = n
s = ''
c = 0
while True:
    if n < 10:  # n이 0보다 작으면 앞에 0을 붙힘 (문자형으로 더해야함)
        n = "0"+str(n)
    n = str(n)  # n을 문자로 바꿔야 index를 지정할 수 있음
    if int(n[0]) + int(n[1]) < 10:  # 각 자릿 수 더한 값이 10보다 작을 때,
        s = str(int(n[0]) + int(n[1]))  # 그대로 받아서 s에 저장
    else:
        s = str(int(n[0]) + int(n[1]))[1]  # 아니면 1의 자리 수만 받기
    n = int(n[1]+s)  # n의 1의 자리 수랑 s를 붙혀주고 반복하여 값을 비교하기 위해 숫자로 형변환
    c += 1  # 반복문이 반복할 때마다 count
    if n == m:  # 반복문안에서 계속 업데이트데는 n과 앞에서 입력한 n을 저장한 m을 비교
        break
print(c)
