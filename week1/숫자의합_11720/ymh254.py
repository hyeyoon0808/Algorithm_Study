numberLength = int(input())
number = list(input())
result = 0
for i in range(0, numberLength):
    result += int(number[i])
print(result)
