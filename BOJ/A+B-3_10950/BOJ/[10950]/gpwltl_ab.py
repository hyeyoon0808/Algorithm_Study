leng = int(input())
total = list()
for i in range(1, leng+1):
    num1, num2 = input().split()
    total.append(int(num1)+int(num2))

for i in range(0, leng):
    print(total[i])
