import re

n = int(input())
lost = input()
lost = list(map(int, re.findall('\d+', lost)))
reverse = input()
reverse = list(map(int, re.findall('\d+', reverse)))

for i in range(len(lost)):
    for j in range(len(reverse)):
        if lost[i]-1 == reverse[j] or lost[i] + 1 == reverse[j]:
            continue
        else:
            n -= 1
print(n)
