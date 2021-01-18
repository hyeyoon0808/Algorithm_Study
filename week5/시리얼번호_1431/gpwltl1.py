import sys
import re
input = sys.stdin.readline


# 문자열 안에 있는 숫자를 뽑아서 더해주는 함수
def sun_num(s):
    # re.findall("\d", string) : 문자열안에 들어있는 숫자만 뽑아 리스트 만들어줌 -> 런타임에러
    # answer = sum(map(int, re.findall("\d", s)))
    answer = 0
    for i in s:
        if i.isdigit() == True:  # 숫자라면?
            answer += int(i)
    return answer


N = int(input())
serial_num = []
for _ in range(N):
    serial_num.append(input().strip())

# 정렬 기준을 sorted와 lambda를 이용하여 3가지 조건을 넣어준다.
serial_num = sorted(serial_num, key=lambda x: (len(x), sun_num(x), x))

for i in serial_num:
    print(i)


# __line 에서 사용한 함수? String.isalpha() -> 문자열 알파벳 구성 여부확인
# String.isdigit() -> 숫자로만 구성된지 여부 확인

# re.findall("\d", string) : 문자열에서 숫자뽑아내기
# "\d+" >> 숫자 묶음 단위별 추출
# "\d"  >> 한자리 숫자 단위별로 추출
