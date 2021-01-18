import re
import sys
input = sys.stdin.readline


def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if len(array[j]) != len(array[j-1]):
                if len(array[j]) < len(array[j-1]):
                    array[j], array[j-1] = array[j-1], array[j]
                else:
                    break

            else:
                # 숫자가 포함된 것만 비교할 때(숫자합 순 정렬)
                if array[j].isalpha() == False and array[j-1].isalpha() == False:
                    x = sum(map(int, re.findall("\d", array[j])))
                    y = sum(map(int, re.findall("\d", array[j-1])))
                    if x < y:
                        array[j], array[j-1] = array[j-1], array[j]
                    else:
                        break

                else:  # 숫자가 포함된게 있거나 문자만 존재할 때(알파벳순 정렬)
                    # 문자열끼리
                    if array[j][0].isalpha() == True and array[j-1][0].isalpha() == True:
                        if array[j] < array[j-1]:
                            array[j], array[j-1] = array[j-1], array[j]
                        else:
                            break
                    else:
                        if array[j] > array[j-1]:
                            array[j], array[j-1] = array[j-1], array[j]
                        else:
                            break
    return array


n = int(input())
serial = []
for _ in range(n):
    a = str(input())
    serial.append(array)

if len(serial) != 0 and len(serial) > 1:
    for i in insert_sort(serial):
        print(i)
elif len(serial) == 1:
    print(serial[0])


# __line 에서 사용한 함수? String.isalpha() -> 문자열 알파벳 구성 여부확인
# String.isdigit() -> 숫자로만 구성된지 여부 확인
