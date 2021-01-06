n = int(input())
score = list(map(int, input().split()))
new = []
total = 0
for i in range(n):
    m = max(score)
    new.append(score[i]/m*100)
for i in range(n):
    total += new[i]
    average = round(total/n, 2)
print(average)
