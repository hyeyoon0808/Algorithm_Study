count = int(input())
num = list(input()) #리스트형으로 input
result = 0
for i in range(count):
    result += int(num[i]) #int로 변환
print(result)

#num을 받을때 map()를 사용하여 int로 미리 받을려 했으나 오류