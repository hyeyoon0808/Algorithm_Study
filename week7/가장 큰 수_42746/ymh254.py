lst = [3, 30, 34, 5, 9]

lst = list(map(str, lst))  # 문자열로 만들기
# 1000이하의 최댓값으로 만든 후 크기를 비교
lst.sort(key=lambda x: x*3, reverse=True)
# 맨 앞이 0일 경우, 즉 0으로만 이뤄진 숫자일 경우(중복을 없애기 위함)
print(str(int("".join(lst))))
