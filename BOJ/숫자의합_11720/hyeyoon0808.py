count = int(input())
num = list(map(int, input())) #리스트형으로 input
result = 0
for i in range(count):
    result += (num[i]) #int로 변환
print(result)
