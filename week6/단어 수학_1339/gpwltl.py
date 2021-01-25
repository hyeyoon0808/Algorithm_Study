import sys
input = sys.stdin.readline

leng = int(input())
arr = [0]*leng
for i in range(leng):
    arr[i] = input().strip()

alpha = {}
answer = 0

for j in range(len(arr)):
    l = len(arr[j])
    for i in arr[j]:
        if i in alpha:  # alpha에 알파벳이 있는지 확인  (if 'key1' in dict:)
            alpha[i] += 10**(l-1)
        else:
            alpha[i] = 10**(l-1)
        l -= 1

alpha1 = sorted(alpha.items(), key=lambda x: x[1], reverse=True)

for i in range(len(alpha1)):
    answer += (9-i)*alpha1[i][1]
print(answer)
