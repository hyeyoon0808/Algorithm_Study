from random import sample
nineP = []

# 9개 받아와서 리스트에 추가
for i in range(9):
    person = int(input())
    nineP.append(person)

while True:
    global sevenP   # while문 밖에서도 리스트를 사용하기 위해 global 붙이기(전역변수 값 변경가능)
    sevenP = sample(nineP, 7)  # nineP 리스트에서 7개의 숫자 랜덤 추출
    # random.sample(리스트, 갯수) - 여러개 랜덤 호출, 중복은 허용x
    if sum(sevenP) == 100:
        break

sevenP.sort()
for i in sevenP:
    print(i)
